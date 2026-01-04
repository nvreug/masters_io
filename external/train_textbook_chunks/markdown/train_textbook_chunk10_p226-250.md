216 _CHAPTER 8. NUMERICAL MAXIMIZATION_


**Step-size**


It is possible for the N-R procedure, as for other procedure below, to
step past the maximum and move to a lower _LL_ ( _β_ ). Figure 8.4 depicts
the situation. The actual _LL_ is given by the solid line. The dotted line
is a quadratic function that has the slope and curvature that _LL_ has
at the point _βt_ . The N-R procedure moves to the top of the quadratic,
to _βt_ +1. However, _LL_ ( _βt_ +1) is lower than _LL_ ( _βt_ ) in this case.



β
_t_



β
_t+1_



![](/Users/nicholasvreugdenhil/ASU Dropbox/Nicholas Vreugdenhil/masters_io_2026/external/train_textbook_chunks/markdown/train_textbook_chunk10_p226-250_images/train_textbook_chunk10_p226-250.pdf-0-0.png)





_LL_ (β )
_t_
_LL_ (β )
_t+1_





Figure 8.4: Step may go beyond maximum to lower _LL_ .


To account for this possibility, the step is multiplied by a scalar _λ_
in the N-R formula:


_βt_ +1 = _βt_ + _λ_ ( _−Ht_ ) _[−]_ [1] _gt._


The vector ( _−Ht_ ) _[−]_ [1] _gt_ is called the direction and _λ_ is called the stepsize. (This terminology is standard even though ( _−Ht_ ) _[−]_ [1] _gt_ contains
step-size information through _Ht_, as explained above in relation to
Figure 8.3.) The step-size _λ_ is reduced to assure that each step of
the N-R procedure provides an increase in _LL_ ( _β_ ). The adjustment is
performed separately in each iteration, as follows.
Start with _λ_ = 1. If _LL_ ( _βt_ +1) _> LL_ ( _βt_ ), move to _βt_ +1 and start a
new iteration. If _LL_ ( _βt_ +1) _< LL_ ( _βt_ ), then set _λ_ = 1 _/_ 2 and try again.
If with _λ_ = 1 _/_ 2, _LL_ ( _βt_ +1) is still below _LL_ ( _βt_ ), then set _λ_ = 1 _/_ 4
and try again. Continue this process until a _λ_ is found for which
_LL_ ( _βt_ +1) _> LL_ ( _βt_ ). If this process results in a tiny _λ_, then little


_8.3. ALGORITHMS_ 217


progress is made in finding the maximum. This can be taken as a
signal to the researcher that a different iteration procedure might be
needed.
An analogous step-size adjustment can be made in the other direction, that is, by increasing _λ_ when appropriate. A case is shown
in Figure 8.5. The top of the quadratic is obtained with a step-size



for λ=4



β β
_t_ _t+1_

for λ=1



β
_t+1_



β _t+1_ β _t+1_

for λ=2 for λ



![](/Users/nicholasvreugdenhil/ASU Dropbox/Nicholas Vreugdenhil/masters_io_2026/external/train_textbook_chunks/markdown/train_textbook_chunk10_p226-250_images/train_textbook_chunk10_p226-250.pdf-1-0.png)





Figure 8.5: Double _λ_ as long as _LL_ rises.


of _λ_ = 1. However, the _LL_ ( _β_ ) is not quadratic and its maximum is
further away. The step-size can be adjusted upward as long as the
_LL_ ( _β_ ) continues to rise. That is, calculate _βt_ +1 with _λ_ = 1 at _βt_ +1. If
_LL_ ( _βt_ +1) _> LL_ ( _βt_ ), then try _λ_ = 2. If the _βt_ +1 based on _λ_ = 2 gives
a higher value of the log-likelihood function than with _λ_ = 1, then try
_λ_ = 4. And so on, doubling _λ_ as long as doing so further raises the
likelihood function. Each time, _LL_ ( _βt_ +1) with a doubled _λ_ is compared
to its value at the previously tried _λ_, rather than with _λ_ = 1, in order
to assure that each doubling raises the likelihood function further than
it had previously been raised with smaller _λ_ ’s. In Figure 8.5, a final
step-size of 2 is used, since the likelihood function with _λ_ = 4 is lower
than when _λ_ = 2, even though it is higher than with _λ_ = 1.
The advantage of this approach of raising _λ_ is that it usually reduces the number of iterations that are needed to reach the maximum.
New values of _λ_ can be tried without re-calculating _gt_ and _Ht_, while
each new iteration requires calculation of these terms. Adjusting _λ_ can


218 _CHAPTER 8. NUMERICAL MAXIMIZATION_


therefore quicken the search for the maximum.


**Concavity**


If the log-likelihood function is globally concave, then the N-R procedure is guaranteed to provide an increase in the likelihood function
at each iteration. This fact is demonstrated as follows. _LL_ ( _β_ ) being
concave means that its Hessian is negative definite at all values of _β_ .
(In one dimension, the slope of _LL_ ( _β_ ) is declining such that the second
derivative is negative.) If _H_ is negative definite, then _H_ _[−]_ [1] is also negative definite, and ( _−H_ _[−]_ [1] ) is positive definite. By definition, a symmetric matrix _M_ is positive definite if _x_ _[′]_ _Mx >_ 0 for any _x ̸_ = 0. Consider
a first-order Taylor’s approximation of _LL_ ( _βt_ +1) around _LL_ ( _βt_ ):


_LL_ ( _βt_ +1) = _LL_ ( _βt_ ) + ( _βt_ +1 _−_ _βt_ ) _[′]_ _gt._


Under the N-R procedure, _βt_ +1 _−_ _βt_ = _λ_ ( _−Ht_ _[−]_ [1] ) _gt_ . Substituting gives:

_LL_ ( _βt_ +1) = _LL_ ( _βt_ ) + ( _λ_ ( _−Ht_ _[−]_ [1] ) _gt_ ) _[′]_ _gt_
= _LL_ ( _βt_ ) + _λgt_ _[′]_ [(] _[−][H]_ _t_ _[−]_ [1] ) _gt._


Since _−H_ _[−]_ [1] is positive definite, the quantity _gt_ _[′]_ [(] _[−][H]_ _t_ _[−]_ [1] ) _gt >_ 0 and
_LL_ ( _βt_ +1) _> LL_ ( _βt_ ). Note that since this comparison is based on a
first-order approximation, an increase in _LL_ ( _β_ ) might only be obtained
in a small neighborhood of _βt_ . That is, the value of _λ_ that provides an
increase might be small. However, an increase is indeed guaranteed at
each iteration if _LL_ ( _β_ ) is globally concave.
Suppose the log-likelihood function has regions that are not concave. In these areas, the N-R procedure can fail to find an increase.
If the function is convex at _βt_, then the N-R procedure moves in the
opposite direction of the slope of the log-likelihood function. The situation is illustrated in Figure 8.6 for _K_ = 1. The N-R step with one
parameter is _LL_ _[′]_ ( _β_ ) _/_ ( _−LL_ _[′′]_ ( _β_ )), where the prime denotes derivatives.
The second derivative is positive at _βt_ since the slope is rising. Therefore, _−LL_ _[′′]_ ( _β_ ) is negative, and the step is in the opposite direction of
the slope. With _K >_ 1, if the Hessian is positive definite at _βt_, then
( _−Ht_ _[−]_ [1] ) is negative definite, and N-R steps in the opposite direction
of _gt_ .
The sign of the Hessian can be reversed in these situations. However, there is no reason for using the Hessian where the function is
not concave, since the Hessian in convex regions does not provide any


_8.3. ALGORITHMS_ 219


β
_t_


Figure 8.6: N-R in convex portion of _LL_ .


useful information on where the maximum might be. There are easier
ways to find an increase in these situations than calculating the Hessian and reversing its sign. This issue is part of the motivation for
other procedures.


The N-R procedure has two drawbacks. First, calculation of the
Hessian is usually computationally intensive. Procedures that avoid
calculating the Hessian at every iteration can be much faster. Second,
as we have just shown, the N-R procedure does not guarantee an increase in each step if the log-likelihood function is not globally concave.
When ( _−Ht_ _[−]_ [1] ) is not positive definite, an increase is not guaranteed.


Other approaches use approximations to the Hessian that address
these two issues. The methods differ in the form of the approximation.
Each procedure defines a step as:


_βt_ +1 = _βt_ + _λMtgt,_


where _Mt_ is a _K ×K_ matrix. For N-R, _Mt_ = _−H_ _[−]_ [1] . Other procedures
use _Mt_ ’s that are easier to calculate than the Hessian and are necessarily positive definite so as to guarantee an increase at each iteration
even in convex regions of the log-likelihood function.



![](/Users/nicholasvreugdenhil/ASU Dropbox/Nicholas Vreugdenhil/masters_io_2026/external/train_textbook_chunks/markdown/train_textbook_chunk10_p226-250_images/train_textbook_chunk10_p226-250.pdf-3-1.png)
220 _CHAPTER 8. NUMERICAL MAXIMIZATION_


**8.3.2** **BHHH**



The N-R procedure does not utilize the fact that the function being
maximized is actually the sum of log-likelihoods over a sample of observations. The gradient and Hessian are calculated just as one would do
in maximizing any function. This characteristic of N-R provides generality, in that the N-R procedure can be used to maximize any function,
not just a log-likelihood. However, as we will see, maximization can
be faster if we utilize the fact that the function being maximized is a
sum of terms in a sample.
We need some additional notation to reflect the fact that the loglikelihood function is a sum over observations. The score of an observation is the derivative of that observation’s log likelihood with respect
to the parameters: _sn_ ( _βt_ ) = _∂lnPn_ ( _β_ ) _/∂β_ evaluated at _βt_ . The gradient, which we defined above and used for the N-R procedure, is the
average score: _gt_ = [�] _n_ _[s][n]_ [(] _[β][t]_ [)] _[/N]_ [. The outer product of observation]
_n_ ’s score is the _K × K_ matrix:



_s_ [1] _n_ _[s]_ [1] _n_ _s_ [1] _n_ _[s]_ [2] _n_ _· · ·_ _s_ [1] _n_ _[s][K]_ _n_
_s_ [1] _n_ _[s]_ [2] _n_ _s_ [2] _n_ _[s]_ [2] _n_ _· · ·_ _s_ [2] _n_ _[s][K]_ _n_

_· · ·_
_s_ [1] _n_ _[s][K]_ _n_ _s_ [2] _n_ _[s][K]_ _n_ _· · ·_ _s_ _[K]_ _n_ _[s]_ _n_ _[K]_













_sn_ ( _βt_ ) _sn_ ( _βt_ ) _[′]_ =













where _s_ _[k]_ _n_ [is the] _[ k]_ [-th element of] _[ s][n]_ [(] _[β][t]_ [) with the dependence on] _[ β][t]_
omitted for convenience. The average outer product in the sample is
_Bt_ = [�] _n_ _[s][n]_ [(] _[β][t]_ [)] _[s][n]_ [(] _[β][t]_ [)] _[′][/N]_ [. This average outer product is related to]
the covariance matrix: if the average score were zero, then B would
be the covariance matrix of scores in the sample. Often _Bt_ is called
the “outer product of the gradient.” This term can be confusing since
_Bt_ is not the outer product of _gt_ . However, the term reflects the fact
that the score is an observation-specific gradient and _Bt_ is the average
outer product of these observation-specific gradients.
At the parameters that maximize of the likelihood function, the
average score is indeed zero. The maximum occurs where the slope is
zero, which means that the gradient, i.e., the average score, is zero.
Since the average score is zero, the outer product of the scores, _Bt_,
becomes the variance of the scores. That is, at the maximizing values
of the parameters, _Bt_ is the variance of scores in the sample.
The variance of the scores provides important information for locating the maximum of the likelihood function. In particular, this variance provides a measure of the curvature of the log-likelihood function,


_8.3. ALGORITHMS_ 221


similar to the Hessian. Suppose that everyone in the sample has similar scores. Since everyone is fairly similar, the sample contains very
little information. The log-likelihood function is fairly flat in this situation, reflecting the fact that the sample contains little information
such that different values of the parameters fit the data about the same.
The first panel of Figure 8.7 depicts this situation: with a fairly flat
log-likelihood, different values of _β_ give similar values of _LL_ ( _β_ ). The



![](/Users/nicholasvreugdenhil/ASU Dropbox/Nicholas Vreugdenhil/masters_io_2026/external/train_textbook_chunks/markdown/train_textbook_chunk10_p226-250_images/train_textbook_chunk10_p226-250.pdf-5-0.png)



![](/Users/nicholasvreugdenhil/ASU Dropbox/Nicholas Vreugdenhil/masters_io_2026/external/train_textbook_chunks/markdown/train_textbook_chunk10_p226-250_images/train_textbook_chunk10_p226-250.pdf-5-1.png)



Figure 8.7: Shape of log-likelihood function near maximum.


curvature is small when the variance of the scores is small. Conversely,
the scores differing greatly over observations means that the observations are quite different and the sample provides considerable amount
of information. The log-likelihood function is highly peaked, reflecting
the fact that the sample provides good information on the values of
_β_ . Moving away from the maximizing values of _β_ causes a large loss
of fit. The second panel of Figure 8.7 illustrates this situation. The
curvature is great when the variance of the scores is high.
These ideas about the variance of the scores and their relation
to the curvature of the log-likelihood function are formalized in the
famous “information identity.” This identity states that the covariance
of the scores at the true parameters is equal to the negative of the
expected Hessian. We demonstrate this identity in the last section of
this chapter; Theil (1971) and Ruud (2000) also provide useful and
heuristic proofs. However, even without proof, it makes intuitive sense
that the variance of the scores provides information on the curvature
of the log-likelihood function.
Berndt, Hall, Hall and Hausman (1974), hereafter referred to as
BHHH (and commonly pronounced B-triple H), proposed using this relationship in the numerical search for the maximum of the log-likelihood


222 _CHAPTER 8. NUMERICAL MAXIMIZATION_


function. In particular, the BHHH procedure uses _Bt_ in the optimization routine in place of _−Ht_ . Each iteration is defined by:


_βt_ +1 = _βt_ + _λBt_ _[−]_ [1] _gt._


This step is the same as for N-R except that _Bt_ is used in place of _−Ht_ .
Given the discussion above about the variance of the scores indicating
the curvature of the log-likelihood function, replacing _−Ht_ with _Bt_
makes sense.
There are two advantages to the BHHH procedure over N-R:
(1) _Bt_ is far faster to calculate that _Ht_ . The scores must be calculated to obtain the gradient for the N-R procedure anyway, and so
calculating _Bt_ as the average outer product of the scores takes hardly
any extra computer time. In contrast, calculating _Ht_ requires calculating the second derivatives of the log-likelihood function.
(2) _B_ is necessarily positive definite. The BHHH procedure is therefore guaranteed to provide an increase in _LL_ ( _β_ ) in each iteration, even
in convex portions of the function. Using the proof given above for NR when _−Ht_ is positive definite, the BHHH step _λBt_ _[−]_ [1] _gt_ raises _LL_ ( _β_ )
for a small enough _λ_ .
Our discussion about the relation of the variance of the scores to the
curvature of the log-likelihood function can be stated a bit more precisely. For a correctly specified model at the true parameters, _B →−H_
as _N →∞_ . This relation between the two matrices is an implication of
the information identity, discussed at greater length in the last section.
This convergence suggests that _Bt_ can be considered an approximation
to _−Ht_ . The approximation is expected to be better as sample size
rises. And the approximation can be expected to be better close to the
true parameters, where the expected score is zero and the information
identity holds, than for values of _β_ that are farther from their true
values. That is, _Bt_ can be expected to be a better approximation close
to the maximum of the _LL_ ( _β_ ) than farther from the maximum.
There are some drawbacks of BHHH. The procedure can give small
steps that raise _LL_ ( _β_ ) very little, especially when the iterative process
is far from the maximum. This behavior can arise because _Bt_ is not a
good approximation to _−Ht_ far from the true value. Or it might arise
because _LL_ ( _β_ ) is highly non-quadratic in the area where the problem
is occurring. If the function is highly non-quadratic, N-R does not perform well as explained above; since BHHH is an approximation to N-R,


_8.3. ALGORITHMS_ 223


BHHH would not perform well even if _Bt_ were a good approximation
to _−Ht_ .


**8.3.3** **BHHH-2**


The BHHH procedure relies on the matrix _Bt_ which, as we have described, captures the covariance of the scores when the average score
is zero (i.e., at the maximizing value of _β_ .) When the iterative process
is not at the maximum, the average scores is not zero and _Bt_ does not
represent the covariance of the scores.
A variant on the BHHH procedure is obtained by subtracting out
the mean score before taking the outer product. For any level of the
average score, the covariance of the scores over the sampled decisionmakers is

    _Wt_ = ( _sn_ ( _βt_ ) _−_ _gt_ )( _sn_ ( _βt_ ) _−_ _gt_ ) _[′]_ _/N_

_n_


where the gradient _gt_ is the average score. _Wt_ is the covariance of the
scores around their mean, and _Bt_ is the average outer product of the
scores. _Wt_ and _Bt_ are the same when the mean gradient is zero (i.e.,
at the maximizing value of _β_ ), but differ otherwise.
The maximization procedure can use _Wt_ instead of _Bt_ :


_βt_ +1 = _βt_ + _λWt_ _[−]_ [1] _gt._


This procedure, which I call BHHH-2, has the same advantages as
BHHH. _Wt_ is necessarily positive definite, since it proportional to a
covariance matrix, and so the procedure is guaranteed to provide an
increase in _LL_ ( _β_ ) at every iteration. Also, for a correctly specified
model at the true parameters, _W →−H_ as _N →∞_, such that _Wt_
can be considered an approximation to _−Ht_ . The information identity
establishes this equivalence, as for _B_ .
For _β_ ’s that are close to the maximizing value, BHHH and BHHH-2
give nearly the same results. They can differ greatly at values far from
the maximum. Experience indicates, however, that the two methods
are fairly similar in that either both of them work effectively for a given
likelihood function, or neither of them does. The main value of BHHH2 is pedagogical, to elucidate the relation between the covariance of
the scores and the average outer product of the scores. This relation is
critical in the analysis of the information identity in the last section.


224 _CHAPTER 8. NUMERICAL MAXIMIZATION_


**8.3.4** **Steepest Ascent**


This procedure is defined by the iteration formula:


_βt_ +1 = _βt_ + _λgt._


The defining matrix for this procedure is the identity matrix _I_ . Since _I_
is positive definite, the method guarantees an increase in each iteration.
It is called “steepest ascent” because it provides the greatest possible
increase in _LL_ ( _β_ ) for the distance between _βt_ and _βt_ +1, at least for
small enough distance. Any other step of the same distance provides
less increase. This fact is demonstrated as follows. Take a first-order
Taylor’s expansion of _LL_ ( _βt_ +1) around _LL_ ( _βt_ ): _L_ ( _βt_ +1) = _βt_ +( _βt_ +1 _−_
_βt_ ) _gt._ Maximize this expression for _√ LL_ ( _βt_ +1) subject to the Euclidian
distance from _βt_ to _βt_ +1 being _k_ . That is, maximize subject to

( _βt_ +1 _−_ _βt_ ) _[′]_ ( _βt_ +1 _−_ _βt_ ) = _k_ . The Lagrangian is


L = _LL_ ( _βt_ ) + ( _βt_ +1 _−_ _βt_ ) _gt −_ [1]

2 _λ_ [[(] _[β][t]_ [+1] _[ −]_ _[β][t]_ [)] _[′]_ [(] _[β][t]_ [+1] _[ −]_ _[β][t]_ [)] _[ −]_ _[k]_ []]


_∂_ L
= _gt −_ [1]
_∂βt_ +1 _λ_ [(] _[β][t]_ [+1] _[ −]_ _[β][t]_ [) = 0]

_βt_ +1 _−_ _βt_ = _λgt_
_βt_ +1 = _βt_ + _λgt_


which is the formula for steepest ascent.
While at first encounter, one might think that the method of steepest ascent is the best possible procedure since it gives the greatest possible increase in the log-likelihood function at each step. However, the
method’s property is actually less grand than this statement implies.
Note that the derivation relies on a first-order approximation that is
only accurate in a neighborhood of _βt_ . The correct statement of the
result is that there is some sufficiently small distance for which the
method of steepest ascent gives the greatest increase for that distance.
This distinction is critical. Experience indicates that the step-sizes
are often very small with this method. The fact that the ascent is
greater than for any other step of the same distance is not particularly
comforting when the steps are so small. Usually, BHHH and BHHH-2
converge more quickly than the method of steepest ascent.


_8.3. ALGORITHMS_ 225


**8.3.5** **DFP and BFGS**


The methods of Davidon-Fletcher-Powell (DFP) and Broyden-FletcherGoldfarb-Shanno (BFGS) calculate the approximate Hessian is a way
that uses information at more than one point on the likelihood function. Recall that N-R uses the actual Hessian at _βt_ to determine the
step to _βt_ +1, and BHHH and BHHH-2 use the gradient matrix at _βt_ to
approximate the Hessian. Only information at _βt_ is being used to determine the step in these procedures. If the function is quadratic, then
information at one point on the function provides all the information
that is needed about the shape of the function. These methods work
well, therefore, when the log-likelihood function is close to quadratic.
In contrast, the DFP and BFGS procedures use information at several
points to obtain a sense of the curvature of the log-likelihood function.

The Hessian is the matrix of second derivatives. As such, it gives
the amount by which the slope of the curve changes as one moves along
the curve. The Hessian is defined for infinitesimally small movements.
Since we are interested in making large steps, understanding how the
slope changes for non-infinitesimal movements is useful. An “arc” Hessian can be defined on the basis of how the gradient changes from one
point to another. For example, for function _f_ ( _x_ ), suppose the slope at
_x_ = 3 is 25 and at _x_ = 4 the slope is 19. The change in slope for a one
unit change in _x_ is _−_ 6. In this case, the arc Hessian is _−_ 6, representing
the change in the slope as a step is taken from _x_ = 3 to _x_ = 4.

The procedures of DFP and BFGS use these concepts to approximate the Hessian. The gradient is calculated at each step in the iteration process. The difference in the gradient between the various points
that have been reached is used to calculate an arc Hessian over these
points. This arc Hessian reflects the actual change in gradient that
occurs for actual movement on the curve, as opposed to the Hessian
which simply reflects the change in slope for infinitesimally small steps
around that point. When the log-likelihood function is non-quadratic,
the Hessian at any point provides little information about the shape
of the function. The arc Hessian provides better information.

At each iteration, the DFP and BFGS procedures update the arc
Hessian using information that is obtained at the new point, that is,
using the new gradient. The two procedures differ in how the updating in performed; see Greene (2000) for details. Both methods are
extremely effective, usually far more efficient that N-R, BHHH, BHHH

226 _CHAPTER 8. NUMERICAL MAXIMIZATION_


2, or steepest ascent. BFGS refines DFP, and my experience indicates
that it nearly always works better. BFGS is the default algorithm in
the optimization routines of many commercial software packages.

### **8.4 Convergence criterion**


In theory the maximum of _LL_ ( _β_ ) occurs when the gradient vector is
zero. In practice, the calculated gradient vector is never exactly zero:
it can be very close, but a series of calculations on a computer cannot
produce a result of exactly zero (unless of course, the result is set to
zero through a Boolean operator or by multiplication by zero, neither
of which arises in calculation of the gradient.) The question arises:
when are we sufficiently close to the maximum to justify stopping the
iterative process?
The statistic _mt_ = _gt_ _[′]_ [(] _[−][H]_ _t_ _[−]_ [1] ) _gt_ is often used to evaluate convergence. The researcher specifies a small value for _m_, such as ˘ _m_ = _._ 0001,
and determines in each iteration whether _gt_ _[′]_ [(] _[−][H]_ _t_ _[−]_ [1] ) _gt <_ ˘ _m_ . If this
inequality is satisfied, the iterative process stops and the parameters
at that iteration are considered the converged values, that is, the estimates. For procedures other than N-R that use an approximate Hessian in the iterative process, the approximation is used in the convergence statistic to avoid calculating the actual Hessian. Close to the
maximum, where the criterion becomes relevant, each form of approximate Hessian that we have discussed is expected to be similar to the
actual Hessian.
The statistic _mt_ is the test statistic for the hypothesis that all
elements of the gradient vector are zero. The statistic is distributed
chi-squared with _K_ degrees of freedom. However, the convergence
criterion ˘ _m_ is usually set far more stringently (that is, lower) than the
critical value of a chi-squared at standard levels of significance, so as to
assure that the estimated parameters are very close to the maximizing
values. Usually, the hypothesis that the gradient elements are zero
cannot be rejected for a relatively wide area around the maximum. The
distinction can be illustrated for an estimated coefficient that has a tstatistic of 1.96. The hypothesis cannot be rejected that this coefficient
is any value between zero and twice its estimated value. However,
we would not want convergence to be defined as having reached any
parameter value within this range.
It is tempting to view small changes in _βt_ from one iteration to the


_8.5. LOCAL VERSUS GLOBAL MAXIMUM_ 227


next, and correspondingly small increases in _LL_ ( _βt_ ), as evidence that
convergence has been achieved. However, as stated above, the iterative
procedures may produce small steps because the likelihood function is
not close to a quadratic rather than because of nearing the maximum.
Small changes in _βt_ and _LL_ ( _βt_ ) accompanied by a gradient vector that
is not close to zero indicates that the numerical routine is not effective
at finding the maximum.


Convergence is sometimes assessed on the basis of the gradient
vector itself rather than through the test statistic _mt_ . There are two
procedures: (1) determine whether each element of the gradient vector
is smaller in magnitude than some value that the researcher specifies,
and (2) divide each element of the gradient vector by the corresponding
element of _β_ and determine whether each of these quotients is smaller
in magnitude than some value specified by the researcher. The second approach normalizes for the units of the parameters, which are
determined by the units of the variables that enter the model.

### **8.5 Local versus global maximum**


All of the methods that we have discussed are susceptible to converging
at a local maximum that is not the global maximum, as shown in Figure
8.8. When the log-likelihood function is globally concave, as for logit
with linear-in-parameters utility, then there is only one maximum and
the issue doesn’t arise. However, most discrete choice models are not
globally concave.


A way to investigate the issue is to use a variety of starting values
and observe whether convergence occurs at the same parameter values.
For example, in Figure 8.8, starting at _β_ 0 will lead to convergence
at _β_ 1. Unless other starting values were tried, the researcher would
mistakenly believe that the maximum of _LL_ ( _β_ ) had been achieved.
Starting at _β_ 2, convergence is achieved at _β_ [ˆ] . By comparing the _LL_ ( _β_ [ˆ] )
with _LL_ ( _β_ 1), the researcher finds that _β_ 1 is not the maximizing value.
Liu and Mahmassani (2000) propose a way to select starting values
that involves the researcher setting upper and lower bounds on each
parameter and randomly choosing values within those bounds.


228 _CHAPTER 8. NUMERICAL MAXIMIZATION_


β0 β1 β _[^]_ β2

β


Figure 8.8: Local versus global maximum

### **8.6 Variance of the Estimates**


In standard econometric courses, it is shown that, for a correctly specified model,
_√_

_N_ ( _β_ [ˆ] _−_ _β_ _[∗]_ ) _→_ _[d]_ N(0 _,_ ( _−_ **H** ) _[−]_ [1] )


as _N →∞_, where _β_ _[∗]_ is the true parameter vector, _β_ [ˆ] is the maximum
likelihood estimator, and **H** is the expected Hessian in the population.
The negative of the expected Hessian, _−_ **H**, is often called the information matrix. Stated in words: the sampling distribution of the difference between the estimator and the true value, normalized for sample
size, converges asymptotically to a normal distribution centered on
zero and with covariance equal to the inverse of the information ma_√_
trix, _−_ **H** _[−]_ [1] . Since the asymptotic covariance of _N_ ( _β_ [ˆ] _−_ _β_ _[∗]_ ) is _−_ **H** _[−]_ [1],

the asymptotic covariance of _β_ [ˆ] itself is _−_ **H** _[−]_ [1] _/N_ .
The bold-face type in these expressions indicates that **H** is the average in the population, as opposed to _H_ which is the average Hessian
in the sample. The researcher calculates the asymptotic covariance by
using _H_ as an estimate of **H** . That is, the asymptotic covariance of _β_ [ˆ]
is calculated as _−H_ _[−]_ [1] _/N_ where _H_ is evaluated at _β_ [ˆ] .
Recall that _W_ is the covariance of the scores in the sample. At the
maximizing values of _β_, _B_ is also the covariance of the scores. By the
information identity discussed above and explained in the last section,
_−H_, which is the (negative of the) average Hessian in the sample,



![](/Users/nicholasvreugdenhil/ASU Dropbox/Nicholas Vreugdenhil/masters_io_2026/external/train_textbook_chunks/markdown/train_textbook_chunk10_p226-250_images/train_textbook_chunk10_p226-250.pdf-12-0.png)
_8.7. INFORMATION IDENTITY_ 229


converges to the covariance of the scores for a correctly specified model
at the true parameters. In calculating the asymptotic covariance of the
estimates _β_ [ˆ], any of these three matrices can be used as an estimate of

_−_ **H** . The asymptotic variance of _β_ [ˆ] is calculated as _W_ _[−]_ [1] _/N_, _B_ _[−]_ [1] _/N_,
or _−H_ _[−]_ [1] _/N_, where each of these matrices is evaluated at _β_ [ˆ] .
If the model is not correctly specified, then the asymptotic covariance of _β_ [ˆ] is more complicated. In particular, for any model for which
the expected score is zero at the true parameters,
_√_

_N_ ( _β_ [ˆ] _−_ _β_ _[∗]_ ) _→_ _[d]_ N(0 _,_ **H** _[−]_ [1] **VH** _[−]_ [1] )


where **V** is the variance of the scores in the population. When the
model is correctly specified, the matrix _−_ **H** = **V** by the information
identity, such that **H** _[−]_ [1] **VH** _[−]_ [1] = _−_ **H** _[−]_ [1] and we get the formula for
a correctly specified model. However, if the model is not correctly
specified, this simplification does not occur. The asymptotic distribution of _β_ [ˆ] is **H** _[−]_ [1] **VH** _[−]_ [1] _/N_ . This matrix is called the ”robust covariance
matrix” since it is valid whether or not the model is correctly specified.
To estimate the robust covariance matrix, the researcher must calculate the Hessian _H_ . If a procedure other than N-R is being used to
reach convergence, the Hessian need not be calculated at each iteration; however, it must be calculated at the final iteration. Then the
asymptotic covariance is calculated as _H_ _[−]_ [1] _WH_ _[−]_ [1], or with _B_ instead
of _W_ . This formula is sometimes called the “sandwich” estimator of
the covariance, since the Hessian-inverse appears on both sides.

### **8.7 Information Identity**


The information identity states that, for a correctly specified model at
the true parameters, **V** = _−_ **H** where **V** is the covariance of the scores
in the population and **H** is the average Hessian in the population. The
score for a person is the vector of first derivatives of the the person’s
_lnP_ ( _β_ ) with respect to the parameters, and the Hessian is the matrix of second derivatives. The information identity states that, in the
population, the covariance of the first derivatives equals the average
second derivatives (actually, the negative of these second derivatives.)
This is a startling fact, not something that would be expected or even
believed if there were not proof. It has implications throughout econometrics. The implications that we have used in the previous sections
of this chapter are easily derivable from the identity. In particular:


230 _CHAPTER 8. NUMERICAL MAXIMIZATION_


(1) _At the maximizing value of β, W →−H as N →∞, where W_
_is the sample covariance of the scores and H is the sample average of_
_each observation’s Hessian._ As sample size rises, the sample covariance
approaches the population covariance: _W →_ **V** . Similarly, the sample
average of the Hessian approaches the population average: _H →_ **H** .
Since **V** = _−_ **H** by the information identity, _W_ approaches the same
matrix that _−H_ approaches, and so they approach each other.

(2) _At the maximizing value of β, B →−H as N →∞, where_
_B is the sample average of the outer product of the scores._ At _β_ [ˆ], the
average score in the sample is zero, such that _B_ is the same as _W_ . The
result for _W_ applies for _B_ .

We now demonstrate the information identity. We need to expand our notation to account for the population instead of simply the
sample. Let _Pi_ ( _x, β_ ) be the probability that a person who faces explanatory variables _x_ chooses alternative _i_ given the parameters _β_ .
Of the people in the population who face variables _x_, the share who
choose alternative _i_ is this probability calculated at the true parameters: _Si_ ( _x_ ) = _Pi_ ( _x, β_ _[∗]_ ) where _β_ _[∗]_ are the true parameters. Consider
now the gradient of _lnPi_ ( _x, β_ ) with respect to _β_ . The average gradient
in the population is



��
**g** =


_i_



_∂lnPi_ ( _x, β_ )

_Si_ ( _x_ ) _f_ ( _x_ ) _dx_ (8.2)
_∂β_



where _f_ ( _x_ ) is the density of explanatory variables in the population.
This expression can be explained as follows. The gradient for people
who face _x_ and choose _i_ is _∂lnPni_ ( _β_ ) . The average gradient is the

_∂β_
average of this term over all values of _x_ and all alternatives _i_ . The
share of people who face a given value of _x_ is given by _f_ ( _x_ ), and the
share of people who face this _x_ that choose _i_ is _Si_ ( _x_ ). So, _Si_ ( _x_ ) _f_ ( _x_ )
is the share of the population who face _x_ and choose _i_ and therefore
have gradient _[∂lnP][i]_ [(] _[x,β]_ [)] . Summing this term over all values of _i_ and

_∂β_
integrating over all values of _x_ (assuming the _x_ ’s are continuous) gives
the average gradient, as expressed in (8.2).


The average gradient in the population is equal to zero at the true
parameters. This fact can be considered either the definition of the
true parameters or the result of a correctly specified model. Also, we
know that _Si_ ( _x_ ) = _Pi_ ( _x, β_ _[∗]_ ). Substituting these facts into (8.2), we


_8.7. INFORMATION IDENTITY_ 231



have:



��
0 =


_i_



_∂lnPi_ ( _x, β_ )

_Pi_ ( _x, β_ ) _f_ ( _x_ ) _dx,_
_∂β_



where all terms are evaluated at _β_ _[∗]_ . We now take the derivative of
this equation with respect to the parameters:




_[i]_ [(] _[x, β]_ [)] _∂Pi_ ( _x, β_ )

_∂β_ _∂β_ _[′]_







��
0 =


_i_




_∂_ [2] _lnPi_ ( _x, β_ )



_lnPi_ ( _x, β_ )

_Pi_ ( _x, β_ ) + _[∂lnP][i]_ [(] _[x, β]_ [)]
_∂β∂β_ _[′]_ _∂β_



_∂β_ _[′]_



_f_ ( _x_ ) _dx._



Since _∂lnP/∂β_ = (1 _/P_ ) _∂P/∂β_ by the rules of derivatives, we can
substitute _∂_ _[lnP][i]_ [(] _[x,β]_ ~~_[′]_~~ [)] _Pi_ ( _x, β_ ) for _[∂P][i]_ [(] _[x,β]_ ~~_[′]_~~ [)] in the last term in parentheses:



_∂β_ _[i]_ [(] _[x,β]_ ~~_[′]_~~ [)] _Pi_ ( _x, β_ ) for _[∂P]_ _∂β_ _[i]_ [(] _[x,β]_ ~~_[′]_~~ [)]




_[i]_ in the last term in parentheses:

_∂β_ ~~_[′]_~~




_[i]_ [(] _[x, β]_ [)] _∂lnPi_ ( _x, β_ )

_∂β_ _∂β_ _[′]_







��
0 =


_i_




_∂_ [2] _lnPi_ ( _x, β_ )



_lnPi_ ( _x, β_ )

_Pi_ ( _x, β_ ) + _[∂lnP][i]_ [(] _[x, β]_ [)]
_∂β∂β_ _[′]_ _∂β_



_Pi_ ( _x, β_ )
_∂β_ _[′]_



_f_ ( _x_ ) _dx._



Rearranging,



��

_−_


_i_



_lnPi_ ( _x, β_ ) ��

_Pi_ ( _x, β_ ) _f_ ( _x_ ) _dx_ =
_∂β∂β_ _[′]_



_i_



_i_ ( _x, β_ ) _∂lnPi_ ( _x, β_ )

_∂β_ _∂β_ _[′]_



_∂_ [2] _lnPi_ ( _x, β_ )



_∂lnPi_ ( _x, β_ )



_Pi_ ( _x, β_ ) _f_ ( _x_ ) _dx._
_∂β_ _[′]_



Since all terms are evaluated at the true parameters, we can replace
_Pi_ ( _x, β_ ) with _Si_ ( _x_ ) to obtain:



��

_−_


_i_



_lnPi_ ( _x, β_ ) ��

_Si_ ( _x_ ) _f_ ( _x_ ) _dx_ =
_∂β∂β_ _[′]_



_i_



_i_ ( _x, β_ ) _∂lnPi_ ( _x, β_ )

_∂β_ _∂β_ _[′]_



_∂_ [2] _lnPi_ ( _x, β_ )



_∂lnPi_ ( _x, β_ )



_Si_ ( _x_ ) _f_ ( _x_ ) _dx._
_∂β_ _[′]_



The left hand side is the negative of the average Hessian in the population, _−_ **H** . The right hand side is the average outer product of the
gradient, which is the covariance of the gradient since the average gradient is zero: **V** . Therefore, _−_ **H** = **V**, the information identity. As
stated above, the matrix _−_ **H** is often called the information matrix.


232 _CHAPTER 8. NUMERICAL MAXIMIZATION_


## **Chapter 9**

# **Drawing from Densities**

### **9.1 Introduction**

Simulation consists of drawing from a density, calculating a statistic
for each draw, and averaging the results. In all cases, the researcher

                        wants to calculate an average of the form _t_ [¯] = _t_ ( _ε_ ) _f_ ( _ε_ ) _dε_, where _t_ ( _·_ )
is a statistic of interest and _f_ ( _·_ ) is a density. To approximate this
average through simulation, the researcher must be able to take draws
from the density _f_ ( _·_ ). For some densities, this task is simple. However,
in many situations, it is not immediately clear how to draw from the
relevant density. Furthermore, even with simple densities, there might
be ways of taking draws that provide a better approximation to the
integral than a sequence of purely random draws.


We explore these issues in this chapter. In the first sections, we
describe the most prominent methods that have been developed for
taking purely random draws from various kinds of densities. These
methods are presented in a progressive sequence, starting with simple procedures that work with a few convenient densities and moving
to ever more complex methods that work with less convenient densities. The discussion culminates with the Metropolis-Hastings algorithm, which can be used with (practically) any density. The chapter
then turns to the question of whether and how a sequence of draws can
be taken that provides a better approximation to the relevant integral
than a purely random sequence. We discuss antithetics, systematic
sampling, and Halton sequences and show the value that these types
of draws provide in estimation of model parameters.


233


234 _CHAPTER 9. DRAWING FROM DENSITIES_

### **9.2 Random Draws**


**9.2.1** **Standard normal and uniform**


If the researcher wants to take a draw from a standard normal density
(that is, a normal with zero mean and unit variance) or a standard
uniform density (uniform between 0 and 1), the process from a programming perspective is very easy. Most statistical packages contain
random number generators for these densities. The researcher simply
calls these routines to obtain a sequence of random draws. In the sections below, we refer to a draw of a standard normal as _η_ and a draw
of a standard uniform as _µ_ .

The draws from these routines are actually called “pseudo-random
numbers” because nothing that a computer does is truly random.
There are many issues involved in the design of these routines. The
intent in their design is to produce numbers that exhibit the properties
of random draws. The extent to which this intent is realized depends,
of course, on how one defines the properties of “random” draws. These
properties are difficult to define precisely since randomness is a theoretical concept that has no operational counterpart in the real world.
From a practical perspective, my advice is the following: unless one
is willing to spend considerable time investigating and resolving (literally, re-solving) these issues, it is probably better to use the available
routines rather than write a new one.


**9.2.2** **Transformations of standard normal**


Some random variables are transformations of a standard normal. For
example, a draw from a normal density with mean _b_ and variance
_s_ [2] is obtained as _ε_ = _b_ + _sη_ . A draw from a lognormal density is
obtained by exponentiating a draw from a normal density: _ε_ = _e_ [(] _[b]_ [+] _[sη]_ [)] .
The moments of the lognormal are functions of the mean and variance
of the normal that is exponentiated. In particular, the mean of _ε_ is
exp( _b_ + ( _s_ [2] _/_ 2)) and its variance is exp(2 _b_ + _s_ [2] ) _·_ (exp( _s_ [2] ) _−_ 1). Given
values for the mean and variance of the lognormal, the appropriate
values of _b_ and _s_ to use in the transformation can be calculated. It
is more common, however, to treat _b_ and _s_ as the parameters of the
lognormal and calculate its mean and variance from these parameters.


_9.2. RANDOM DRAWS_ 235


**9.2.3** **Inverse cumulative for univariate densities**


Consider a random variable with density _f_ ( _ε_ ) and corresponding cumulative distribution _F_ ( _ε_ ). If _F_ is invertible (that is, if _F_ _[−]_ [1] can be
calculated), then draws of _ε_ can be obtained from draws of a standard
uniform. By definition, _F_ ( _ε_ ) = _k_ means that the probability of obtaining a draw equal to or below _ε_ is _k_, where _k_ is between zero and
one. A draw _µ_ from the standard uniform provides a number between
zero and one. We can set _F_ ( _ε_ ) = _µ_ and solve for the corresponding _ε_ :
_ε_ = _F_ _[−]_ [1] ( _µ_ ). When _ε_ is drawn in this way, the cumulative distribution
of the draws is equal to _F_, such that the draws are equivalent to draws
directly from _F_ . An illustration is provided in Figure 9.1. A draw _µ_ [1]

from a standard uniform translates into the value of _ε_ labeled _ε_ [1], at
which _F_ ( _ε_ [1] ) = _µ_ [1] .


_F_ (ε)


1


µ [1]







_f_ (ε)




|Col1|Col2|
|---|---|
|ε1<br>Area =µ1|ε|



Figure 9.1: Draw of _µ_ [1] from uniform and create _ε_ [1] = _F_ _[−]_ [1] ( _µ_ ).


The extreme value distribution, which is the basis for multinomial
logit models, provides an example. The density is _f_ ( _ε_ ) = exp( _−ε_ ) _·_


236 _CHAPTER 9. DRAWING FROM DENSITIES_


exp( _−_ exp( _−ε_ )) with cumulative distribution _F_ ( _ε_ ) = exp( _−_ exp( _−ε_ )).
A draw from this density is obtained as _ε_ = _−_ ln( _−_ ln( _µ_ )).
Note that this procedure works only for univariate distributions. If
there are two or more elements of _ε_, then _F_ _[−]_ [1] ( _µ_ ) is not unique, since
various combinations of the elements of _ε_ have the same cumulative
probability.


**9.2.4** **Truncated univariate densities**


Consider a random variable that ranges from _a_ to _b_ with density proportional to _f_ ( _ε_ ) within this range. That is, the denisty is (1 _/k_ ) _f_ ( _ε_ ) for _a ≤_
_ε ≤_ _b,_ and 0 otherwise, where _k_ is the normalizing constant that in
                       - _b_
sures that the density integrates to 1: _k_ = _a_ _[g]_ [(] _[ε]_ [)] _[ dε]_ [ =] _[ F]_ [(] _[b]_ [)] _[ −]_ _[F]_ [(] _[a]_ [)] _[.]_
A draw from this density can be obtained by applying the procedure
in section 9.2.3 while assuring that the draw is within the appropriate
range.
Draw _µ_ from a standard uniform density. Calculate the weighted
average of _F_ ( _a_ ) and _F_ ( _b_ ) as ¯ _µ_ = (1 _−_ _µ_ ) _F_ ( _a_ ) + _µF_ ( _b_ ). Then calculate
_ε_ = _F_ _[−]_ [1] (¯ _µ_ ). Since ¯ _µ_ is between _F_ ( _a_ ) and _F_ ( _b_ ), _ε_ is necessarily between
_a_ and _b_ . Essentially, the draw of _µ_ determines how far to go between
_a_ and _b_ . Note that the normalizing constant _k_ is not used in the
calculations and therefore need not be calculated. Figure 9.2 illustrates
the process.


**9.2.5** **Choleski transformation for multivariate normals**


As described in section 9.2.2, a univariate normal with mean _b_ and
variance _s_ [2] is obtained as _ε_ = _b_ + _sµ_ where _µ_ is standard normal. An
analogous procedure can be used to draw from a multivariate normal.
Let _ε_ be a vector with _K_ elements distributed _N_ ( _b,_ Ω). A Choleski factor of Ωis defined as a lower-triangular matrix _L_ such that _LL_ _[′]_ = Ω. It
is often called the generalized square root of Ωor generalized standard
deviation of _ε_ . With _K_ = 1 and variance _s_ [2], the Choleski factor is _s_,
which is just the standard deviation of _ε_ . Most statistical and matrix
manipulation packages have routines to calculate a Choleski factor for
any positive definite, symmetric matrix.
A draw of _ε_ from _N_ ( _b,_ Ω) is obtained as follows. Take _K_ draws
from a standard normal, and label the vector of these draws _η_ =
_⟨η_ 1 _, . . ., ηK⟩_ _[′]_ . Calculate _ε_ = _b_ + _Lη_ . We can verify the properties
of _ε_ . It is normally distributed since the sum of normals is normal.


_9.2. RANDOM DRAWS_ 237


_F_ (ε)


_F_ ( _b_ )


~~µ~~ [1]

_F_ ( _a_ )


_f_ (ε)


|Col1|Col2|
|---|---|
|||
||ε|



_a_ ε [1] _b_





Figure 9.2: Draw of ¯ _µ_ [1] between _F_ ( _a_ ) and _F_ ( _b_ ) gives draw _ε_ [1] from _f_ ( _ε_ )
between _a_ and _b_ .


238 _CHAPTER 9. DRAWING FROM DENSITIES_



Its mean is _b_ : E( _ε_ ) = _b_ + _L_ E( _η_ ) = _b_ . And its covariance is Ω:
Var( _ε_ ) = E( _Lη_ ( _ηL_ ) _[′]_ ) = _L_ E( _ηη_ _[′]_ ) _L_ _[′]_ = _L_ Var( _η_ ) _L_ _[′]_ = _LIL_ _[′]_ = _LL_ _[′]_ = Ω.
To be concrete, consider a three dimensional _ε_ with zero mean. A
draw of _ε_ is calculated as
     















_η_ 1

 _η_ 2
_η_ 3



_ε_ 1

 _ε_ 2
_ε_ 3




















 =



_s_ 11 0 0

 _s_ 21 _s_ 22 0
_s_ 31 _s_ 32 _s_ 33



or
_ε_ 1 = _s_ 11 _η_ 1
_ε_ 2 = _s_ 21 _η_ 1 + _s_ 22 _η_ 2
_ε_ 3 = _s_ 31 _η_ 1 + _s_ 32 _η_ 2 + _s_ 33 _η_ 3 _._

From this we see that Var( _ε_ 1) = _s_ [2] 11 [, Var(] _[ε]_ [2][) =] _[ s]_ 21 [2] [+] _[ s]_ 22 [2] [, and]
Var( _ε_ 3) = _s_ [2] 31 [+] _[ s]_ 32 [2] [+] _[ s]_ 33 [2] [.] Also, Cov( _ε_ 1 _, ε_ 2) = _s_ 11 _s_ 21, and so on.
The elements _ε_ 1 and _ε_ 2 are correlated because of the common influence of _η_ 1 on both of them. They are not perfectly correlated because
_η_ 2 enters _ε_ 2 without affecting _ε_ 1. Similar analysis applies to _ε_ 1 and
_ε_ 3, and _ε_ 2 and _ε_ 3. Essentially, the Choleski factor expresses _K_ correlated terms as arising from _K_ independent components, with each
component “loading” differently onto each term. For any pattern of
covariance, there is some set of loadings from independent components
that reproduces that covariance.


**9.2.6** **Accept-reject for truncated multivariate densities**


The procedure in section 9.2.4 for drawing from truncated densities
applies only to univariate distributions. With multivariate densities,
drawing from a truncated support is more difficult. We describe an
accept-reject procedure that can always be applied. However, as we
will see, there are disadvantages of the approach that might cause a
researcher to choose another approach when possible.
Suppose we want to draw from multivariate density _g_ ( _ε_ ) within the
range _a ≤_ _ε ≤_ _b_ where _a_ and _b_ are vectors with the same length as
_ε_ . That is, we want to draw from _f_ ( _ε_ ) = [1]

_k_ _[g]_ [(] _[ε]_ [) if] _[ a][ ≤]_ _[ε][ ≤]_ _[b,]_ [ and =]
0 otherwise, where _k_ is the normalizing constant. We can obtain draws
from _f_ by simply drawing from _g_ and retaining (“accepting”) the draws
that are within the relevant range and discarding (“rejecting”) the
draws that are outside the range. The advantage of this procedure
is that it can be applied whenever it is possible to draw from the


_9.2. RANDOM DRAWS_ 239


untruncated density. Importantly, the normalizing constant, _k_, does
not need to be known for the truncated density. This fact is useful
since the normalizing constant is usually difficult to calculate.


The disadvantage of the procedure is that the number of draws that
are accepted (that is, the number of draws from _f_ that are obtained)
is not fixed but rather is itself random. If _R_ draws are taken from _g_,
then the expected number of accepts is _kR_ . This expected number is
not known without knowing _k_, which, as stated, is usually difficult to
calculate. It is therefore hard to determine an appropriate number of
draws to take from _g_ . More importantly, the actual number of accepted
draws will generally differ from the expected number. In fact, there is
a positive probability of obtaining no accepts from a fixed number of
draws. When the truncation space is small (or, more precisely, when _k_
is small), obtaining no accepts, and hence no draws from the truncated
density, is a likely event.


This difficulty can be circumvented by drawing from _g_ until a certain number of accepted draws is obtained. That is, instead of setting
in advance the number of draws from _g_ that will be taken, the researcher can set the number of draws from _f_ that are obtained. Of
course, the researcher will not know how long it will take to attain the
set number.


In most situations, other procedures can be applied more easily
to draw from a multivariate truncated density. Nevertheless, it is important to remember that, when nothing else seems possible with a
truncated distribution, the accept-reject procedure can be applied.


**9.2.7** **Importance sampling**


Suppose _ε_ has a density _f_ ( _ε_ ) that cannot be easily drawn from by the
other procedures. Suppose further that there is another density, _g_ ( _ε_ ),
that can easily be drawn from. Draws from _f_ ( _ε_ ) can be obtained as
follows. Take a draw from _g_ ( _ε_ ) and label it _ε_ [1] . Weight the draw by
_f_ ( _ε_ [1] ) _/g_ ( _ε_ [1] ). Repeat this process many times. The set of weighted
draws is equivalent to a set of draws from _f_ .


To verify this fact, we show that the cumulative distribution of the
weighted draws from _g_ is the same as the cumulative distribution of
draws from _f_ . Consider the share of draws from _g_ that are below some


240 _CHAPTER 9. DRAWING FROM DENSITIES_



value _m_, with each draw weighted by _f/g_ . This share is:
�� _f_ ( _ε_ )   -   - _m_   - _f_ ( _ε_ )   



_f_ ( _ε_ )



_g_ ( _ε_ )




- - _m_
_I_ ( _ε < m_ ) _g_ ( _ε_ ) _dε_ =




 - _m_
=




_g_ ( _ε_ ) _dε_



_g_ ( _ε_ )



_−∞_



_f_ ( _ε_ ) _dε_ = _F_ ( _m_ ) _._
_−∞_



In simulation, draws from a density are used to calculate the average of a statistic over that density. Importance sampling can be seen
as a change in the statistic and a corresponding change in the density
that makes the density easy to draw from. Suppose we want to calcu
   late _t_ ( _ε_ ) _f_ ( _ε_ ) _dε_, but find it hard to draw from _f_ . We can multiply
the integrand by _g ÷ g_ without changing its value, such that the inte
    - _f_ ( _ε_ )
gral is _t_ ( _ε_ )

_g_ ( _ε_ ) _[g]_ [(] _[ε]_ [)] _[ dε]_ [. To simulate the integral, we take draws from]
_g_, calculate _t_ ( _ε_ )[ _f_ ( _ε_ ) _/g_ ( _ε_ )] for each draw, and average the results. We
have simply transformed the integral so that it is easier to simulate.
The density _f_ is called the target density, and _g_ is called the proposal density. The requirements for importance sampling are that (1)
the support of _g_ ( _ε_ ) needs to cover the support of _f_, so that any _ε_ that
could arise with _f_ can also arise with _g_, and (2) the ratio _f_ ( _ε_ ) _/g_ ( _ε_ )
must be finite for all values of _ε_, so that this ratio can always be calculated.
A useful illustration of importance sampling arises with multivariate truncated normals. Suppose we want to draw from _N_ (0 _,_ Ω) but
with each element being positive (i.e., truncated below at zero.) The
density is



1
_f_ ( _ε_ ) =



1 1 _e_ [(] _[−]_ 2 [1]
_k_ (2 _π_ ) 2 _[K]_ _|_ Ω _|_ 2




[1] 2 _[ε][′]_ [Ω] _[−]_ [1] _[ε]_ [)]



for _ε ≥_ 0 and 0 otherwise, where _K_ is the dimension of _ε_ and _k_ is the
normalizing constant. (We assume for the purposes of this example
that _k_ is known. In reality, calculating _k_ might take simulation in
itself.) Drawing from this density is difficult because the elements of _ε_
are correlated as well as truncated. However, we can use the procedure
in section 9.2.4 to draw independent truncated normals and then apply
importance sampling to create the correlation. Draw _K_ univariate
normals truncated below at zero, using the procedure in section 9.2.4.
These draws collectively constitute a draw of a _K_ -dimensional vector
_ε_ from the positive quadrant support with density



1
_g_ ( _ε_ ) =



2

1
_m_ (2 _π_ ) 2 _[K]_ _[e]_ [(] _[−]_ [1]




[1] 2 _[ε][′][ε]_ [)]


