266 _CHAPTER 9. DRAWING FROM DENSITIES_



3/4



![](/Users/nicholasvreugdenhil/ASU Dropbox/Nicholas Vreugdenhil/masters_io_2026/external/train_textbook_chunks/markdown/train_textbook_chunk12_p276-300_images/train_textbook_chunk12_p276-300.pdf-0-0.png)



1/2

Sequence



1/2









Transformed
Sequence



1/4


3/4


1/2


1/4



1/3 2/3


Figure 9.19: Randomization of Halton sequence in two dimensions.


_9.3. VARIANCE REDUCTION_ 267


discarding these elements. Two sequences defined by large and similar
primes periodically become “in synch” with each other and stay that
way for many cycles.
Bhat (forthcoming) describes the problem and an effective solution.
Figure 9.20 reproduces a graph from his paper that depicts the Halton
sequence for primes 43 and 47. Cleary, these sequences are highly
correlated.


1



![](/Users/nicholasvreugdenhil/ASU Dropbox/Nicholas Vreugdenhil/masters_io_2026/external/train_textbook_chunks/markdown/train_textbook_chunk12_p276-300_images/train_textbook_chunk12_p276-300.pdf-1-0.png)

0
0 1

Dimension 14



Figure 9.20: Standard Halton sequence.


This correlation can be removed while retaining the desirable coverage of Halton sequences by “scrambling” the digits of each element of
the sequences. The scrambling can be done in various ways. Braatan
and Weller (1979) describe a procedure that is most easily explained
through an example. Consider the Halton sequence for prime 3:



1 [2]
3 _[,]_ 3




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



9 _[, . . . .]_



Recall that the sequence is created by dividing the unit interval into
three segments, which we label A, B, and C in Figure 9.21. Each


268 _CHAPTER 9. DRAWING FROM DENSITIES_


Figure 9.21: Segments for scrambling the Halton sequence.



segment is divided into three subsegments, labeled AA (for subsegment
A of segment A), BA (subsegment B of segment A), CA, AB, BB, CB,
AC, BC, and CC. The Halton sequence is the starting point of each
segment arranged alphbetically and ignoring A (i.e., ignore A, [1]

3 [for B,]
2
3 [for C), followed by the starting point of each subsegment arranged]
alphabetically and ignoring A (i.e., ignore AA, AB and AC, 1
9 [for]
BA, [4] [7] [2] [5] [8]

9 [for BB,] 9 [for BC,] 9 [for CA,] 9 [for CB, and] 9 [for CC.) Note]

that the segments/subsegments starting with A are ignored because
the starting point for those segments/ subsegments are either 0 (for
segment A) or are already included in the sequence (e.g., the starting
point of subsegment AB is the same as the starting point of the segment
B).
The scrambled sequence is obtained by reversing B and C, that is,
by considering C to be before B in the alphabet. The alphabetical
listing is now: segments A C B, subsegments AA AC AB CA CC CB
BA BC BB. The sequence is then created the same way as before but
with this new alphabetical ordering: ignore A, [2] [1]

3 [for C,] 3 [for B, ignore]

AA,AC and AB, [2] [8] [5] [1] [7] [4]

9 [for CA,] 9 [for CC,] 9 [for CB,] 9 [for BA,] 9 [for BC,] 9

for BB. The orginal and scrambled sequences are:




[4] [7]

9 [for BB,] 9




[7] [2]

9 [for BC,] 9




[2] [5]

9 [for CA,] 9




[5] [8]

9 [for CB, and] 9




[7] [4]

9 [for BC,] 9




[2] [8]

9 [for CA,] 9




[8] [5]

9 [for CC,] 9




[5] [1]

9 [for CB,] 9




[2] [1]

3 [for C,] 3




[1] [7]

9 [for BA,] 9



_original_ _scrambled_
1 _/_ 3 2 _/_ 3
2 _/_ 3 1 _/_ 3
1 _/_ 9 2 _/_ 9
4 _/_ 9 8 _/_ 9
7 _/_ 9 5 _/_ 9
2 _/_ 9 1 _/_ 9
5 _/_ 9 7 _/_ 9
8 _/_ 9 4 _/_ 9


Different permutations of the letters are used for different primes.
Figure 9.22, from Bhat (2001), shows the scrambled sequence for primes
43 and 47. The points are not correlated like in the original sequence.


_9.3. VARIANCE REDUCTION_ 269


Bhat demonstrates that scrambled sequences perform well for highdimensional integrals in the same way that unscrambled ones do for
low-dimensional integrals.


1



![](/Users/nicholasvreugdenhil/ASU Dropbox/Nicholas Vreugdenhil/masters_io_2026/external/train_textbook_chunks/markdown/train_textbook_chunk12_p276-300_images/train_textbook_chunk12_p276-300.pdf-3-0.png)

0

Dimension 14



Figure 9.22: Scrambled Halton sequence.


**9.3.6** **Other procedures**


We have described only a few of the most prominent and straightforward antithetic and quasi-random procedures. More complex procedures, with desirable theoretical properties, are described by Niederreiter (1978), Niederreiter (1988), Morokoff and Caflisch (1995), Joe and
Sloan (1993), and Sloan and Wozniakowski (1998), to name only a few
in this burgeoning area of research. As we have seen with Halton sequences, fairly simple procedures can provide large improvements over
random draws. Comparisons performed by S´andor and Andr´as (2001)
on probit and S´andor and Train (2002) on mixed logit indicate that
the accuracy of simulation-based estimation of discrete choice models
can be improved even further with the more complex procedures. It is


270 _CHAPTER 9. DRAWING FROM DENSITIES_


important to remember, however, in the excitement of these methods,
that accuracy can always be improved by simply using more draws.
The researcher needs to decide whether learning and coding new methods of taking draws is more expedient, given her time constraints, than
simply running her model with more draws.


## **Chapter 10**

# **Simulation-Assisted** **Estimation**

### **10.1 Motivation**

So far we have examined how to simulate choice probabilities but have
not investigated the properties of the parameter estimators that are
based on these simulated probabilities. In the applications we have
presented, we simply inserted the simulated probabilities into the loglikelihood function and maximized this function the same as if the
probabilities were exact. This procedure seems intuitively reasonable.
However, we have not actually shown, at least so far, that the resulting
estimator has any desirable properties, such as consistency, asymptotic
normality, or efficiency. We have also not explored the possibility that
other forms of estimation might perhaps be preferable when simulation
is used rather than exact probabilities.
The purpose of this chapter is to examine various methods of estimation in the context of simulation. We derive the properties of
these estimators and show the conditions under which each estimator is consistent and asymptotically equivalent to the estimator that
would arise with exact values rather than simulation. These conditions
provide guidance to the researcher on how the simulation needs to be
performed to obtain desirable properties of the resultant estimator.
The analysis also illuminates the advantages and limitations of each
form of estimation, thereby facilitating the researcher’s choice among
methods.
We consider three methods of estimation:


271


272 _CHAPTER 10. SIMULATION-ASSISTED ESTIMATION_


1. _Maximum Simulated Likelihood:_ _MSL._ This procedure is the
same as maximum likelihood (ML) except that simulated probabilities are used in lieu of the exact probabilities. The properties
of MSL have been derived by, for example, Gourieroux and Monfort (1993), Lee (1995), and Hajivassiliou and Ruud (1994).


2. _Method of Simulated Moments: MSM._ This procedure, suggested
by McFadden (1989), is a simulated analog to the traditional
method of moments (MOM). Under traditional MOM for discrete
choice, residuals are defined as the difference between the 0-1 dependent variable that identifies the chosen alternative and the
probability of the alternative. Exogenous variables are identified
that are uncorrelated with the model residuals in the population.
The estimates are the parameter values that make the variables
and residuals uncorrelated in the sample. The simulated version
of this procedure calculates residuals with the simulated probabilities rather than the exact probabilities.


3. _Method of Simulated Scores: MSS._ As discussed in Chapter 8, the
gradient of the log-likelihood of an observation is called the score
of the observation. The method of scores finds the parameter
values that set the average score to zero. When exact probabilities are used, the method of scores is the same as maximum
likelihood since the log-likelihood function is maximized when
the average score is zero. Hajivassiliou and McFadden (1998)
suggested using simulated scores instead of the exact ones. They
showed that, depending on how the scores are simulated, MSS
can differ from MSL and, importantly, can attain consistency
and efficiency under more relaxed conditions.


In the next section we define these estimators more formally and
relate them to their non-simulated counterparts. We then describe the
properties of each estimator in two stages. First, we derive the properties of the traditional estimator based on exact values. Second, we
show how the derivation changes when simulated values are used rather
than exact values. We show that the simulation adds extra elements
to the sampling distribution of the estimator. The analysis allows us
to identify the conditions under which these extra elements disappear
asymptotically such that the estimator is asymptotically equivalent to
its non-simulated analog. We also identify more relaxed conditions un

_10.2. DEFINITION OF ESTIMATORS_ 273


der which the estimator, though not asymptotically equivalent to its
non-simulated counterpart, is nevertheless consistent.

### **10.2 Definition of estimators**


**10.2.1** **Maximum simulated likelihood: MSL**


The log-likelihood function is

      _LL_ ( _θ_ ) = _lnPn_ ( _θ_ )

_n_


where _θ_ is a vector of parameters, _Pn_ ( _θ_ ) is the (exact) probability
of the observed choice of observation _n_, and the summation is over a
sample of _N_ independent observations. The maximum likelihood (ML)
estimator is the value of _θ_ that maximizes _LL_ ( _θ_ ). Since the gradient of
_LL_ ( _θ_ ) is zero at the maximum, the ML estimator can also be defined
as the value of _θ_ at which

     
_sn_ ( _θ_ ) = 0 _,_
_n_


where _sn_ ( _θ_ ) = _∂lnPn_ ( _θ_ ) _/∂θ_ is the score for observation _n_ .
log-likelihood function isLet _P_ [ˇ] _n_ ( _θ_ ) be a simulated approximation to _SLL_ ( _θ_ ) = [�] _n_ _[ln]_ [ ˇ] _[P][n]_ [(] _P_ _[θ]_ [), and the maximum] _n_ ( _θ_ ). The simulated
simulated likelihood (MSL) estimator is the value of _θ_ that maximizes
_SLL_ ( _θ_ ). Stated equivalently, the estimator is the value of _θ_ at which

_n_ _[s]_ [ˇ] _[n]_ [(] _[θ]_ [) = 0, where ˇ] _[s][n]_ [(] _[θ]_ [) =] _[ ∂ln]_ [ ˇ] _[P][n]_ [(] _[θ]_ [)] _[/∂θ.]_
A preview of the properties of MSL can be given now, with a full
explanation reserved for the next section. The main issue with MSL
arises because of the log transformation. Suppose _P_ [ˇ] _n_ ( _θ_ ) is an unbiased
simulator of _Pn_ ( _θ_ ), such that _ErP_ [ˇ] _n_ ( _θ_ ) = _Pn_ ( _θ_ ) where the expectation
is over draws used in the simulation. All of the simulators that we have
considered are unbiased for the true probability. However, since the
log operation is a non-linear transformation, _lnP_ [ˇ] _n_ ( _θ_ ) is not unbiased
for _lnPn_ ( _θ_ ) even though _P_ [ˇ] _n_ ( _θ_ ) is unbiased for _Pn_ ( _θ_ ). The bias in the
simulator of _lnPn_ ( _θ_ ) translates into bias in the MSL estimator. This
bias diminishes as more draws are used in the simulation.
To determine the asymptotic properties of the MSL estimator, the
question arises of how the simulation bias behaves when sample size
rises. The answer depends critically on the relationship between the


274 _CHAPTER 10. SIMULATION-ASSISTED ESTIMATION_


number of draws that are used in the simulation, labeled _R_, and the
sample size, _N_ . If _R_ is considered fixed, then the MSL estimator
does not converge to the true parameters because of the simulation
bias in _lnP_ [ˇ] _n_ ( _θ_ ). Suppose instead that _R_ rises with _N_ ; that is, the
number of draws rises with sample size. In this case, the simulation
bias disappears as _N_ (and hence _R_ ) rises without bound. MSL is
_√_
consistent in this case. As we will see, if _R_ rises faster than _N_, MSL

is not only consistent but also efficient, asymptotically equivalent to
maximum likelihood on the exact probabilities.
In summary: If _R_ is fixed, then MSL is inconsistent. If _R_ rises at
_√_
any rate with _N_, then MSL is consistent. If _R_ rises faster than _N_,

then MSL is asymptotically equivalent to ML.
The primary limitation of MSL is that it is inconsistent for fixed _R_ .
The other estimators that we consider are motivated by the desire for a
simulation-based estimator that is consistent for fixed _R_ . Both MSM
and MSS, if structured appropriately, attain this goal. This benefit
comes at a price, however, as we see in the discussion below.


**10.2.2** **Method of simulated moments: MSM**


The traditional method of moments (MOM) is motivated by the recognition that the residuals of a model are necessarily uncorrelated in the
population with factors that are exogenous to the behavior being modeled. The MOM estimator is the value of the parameters that make
the residuals in the _sample_ uncorrelated with the exogenous variables.
For discrete choice models, MOM is defined as the parameters that
solve the equation:






_n_





[ _dnj −_ _Pnj_ ( _θ_ )] _znj_ = 0 (10.1)
_j_



where:


_dnj_ is the dependent variable that identifies the chosen alternative:
_dnj_ = 1 if _n_ chose _j_ and zero otherwise, and


_znj_ is a vector of exogenous variables called instruments.


The residuals are [ _dnj_ _−Pnj_ ( _θ_ )], and the MOM estimator is the parameter values at which the residuals are uncorrelated with the instruments
in the sample.


_10.2. DEFINITION OF ESTIMATORS_ 275


This MOM estimator is analogous to MOM estimators for standard
regression models. A regression model takes the form: _yn_ = _x_ _[′]_ _n_ _[β]_ [ +] _[ ε][n]_ [.]
The MOM estimator for this regression is the _β_ at which

    
( _yn −_ _x_ _[′]_ _n_ _[β]_ [)] _[z][n]_ [= 0]
_n_



for a vector of exogenous instruments _zn_ . When the explanatory variables in the model are exogenous, then they serve as the instruments.
The MOM estimator in this case becomes the ordinary least squares
estimator:

  


( _yn −_ _x_ _[′]_ _n_ _[β]_ [)] _[x][n]_ = 0
_n_








- 
_xnyn_ =
_n_ _n_



_xnx_ _[′]_ _n_ _[β]_
_n_








- _−_ 1
��

_xnyn_
_n_



_β_ ˆ =



��



_xnx_ _[′]_ _n_
_n_



_,_



which is the formula for the least squares estimator. When instruments
are specified to be something other than the explanatory variables, the
MOM estimator becomes the standard instrumental variables estimator:

  


( _yn −_ _x_ _[′]_ _n_ _[β]_ [)] _[z][n]_ = 0
_n_








  _znyn_ =
_n_ _n_



_znx_ _[′]_ _n_ _[β]_
_n_








- _−_ 1
��

_znyn_
_n_



_β_ ˆ =



��



_znx_ _[′]_ _n_
_n_



_,_



which is the formula for the instrumental variables estimator. This
estimator is consistent if the instruments are independent of _ε_ in the
population. The estimator becomes more efficient the more highly
correlated the instruments are with the explanatory variables in the
model. When the explanatory variables, _xn_, are themselves exogenous,
then the ideal instruments (i.e., those that give the highest efficiency)
are the explanatory variables themselves, _zn_ = _xn_ .
For discrete choice models, MOM is defined analogously and has
a similar relation to other estimators, especially ML. The researcher
identifies instruments _znj_ that are exogenous and hence independent


276 _CHAPTER 10. SIMULATION-ASSISTED ESTIMATION_


in the population of the residuals [ _dnj −_ _Pnj_ ( _θ_ )]. The MOM estimator
is the value of _θ_ at which the sample correlation between instruments
and residuals is zero. Unlike the linear case, equation (10.1) cannot be
solved explicitly for _θ_ [ˆ] . Instead, numerical procedures are used to find
the value of _θ_ that solves this equation.
As with regression, ML for a discrete choice model is a special case
of MOM. Let the instruments be the scores: _znj_ = _∂lnPnj_ ( _θ_ ) _/∂θ_ . With
these instruments, MOM is the same as ML:


















_n_





_Pnj_ ( _θ_ ) _[∂lnP][nj]_ [(] _[θ]_ [)]

_∂β_

_j_




[ _dnj −_ _Pnj_ ( _θ_ )] _znj_ = 0
_j_



_∂β_






_n_



 [�]



_∂lnPnj_ ( _θ_ )
_dnj_

_∂β_

_j_






 _−_



 [�]



_∂β_



 = 0






_n_



_ni_ ( _θ_ ) _−_  
_∂β_



_n_



1 _∂Pnj_ ( _θ_ )
_Pnj_ ( _θ_ )
_Pnj_ ( _θ_ ) _∂θ_
_j_



= 0
_∂θ_



_∂lnPni_ ( _θ_ )












  _sn_ ( _θ_ ) _−_
_n_ _n_






_j_



_∂Pnj_ ( _θ_ )

= 0
_∂θ_


_sn_ ( _θ_ ) = 0 _,_
_n_



_n_



which is the defining condition for ML. In the third line, _i_ is the chosen
alternative, recognizing that _dnj_ = 0 for all _j ̸_ = _i_ . The fourth line uses
the fact that the sum of _∂Pnj/∂θ_ over alternatives is zero since the
probabilities must sum to 1 before and after the change in _θ_ .
Since MOM becomes ML and hence is fully efficient when the instruments are the scores, the scores are called the ideal instruments.
MOM is consistent whenever the instruments are independent of the
model residuals. It becomes more efficient the higher the correlation
between the instruments and the ideal instruments.
An interesting simplification arises with standard logit. For the
standard logit model, the ideal instruments are the explanatory variables themselves. As shown in (3.7.1), the ML estimator for standard
logit is the value of _θ_ that solves [�] _n_ - _j_ [[] _[d][nj][ −]_ _[P][nj]_ [(] _[θ]_ [)]] _[x][nj]_ [ = 0 where]
_xnj_ are the explanatory variables. This is a MOM estimator with the
explanatory variables as instruments.
A simulated version of MOM, called method of simulated moments
(MSM), is obtained by replacing the exact probabilities _Pnj_ ( _θ_ ) with
simulated probabilities _P_ [ˇ] _nj_ ( _θ_ ). The MSM estimator is the value of _θ_


_10.2. DEFINITION OF ESTIMATORS_ 277



that solves:

    

_n_





[ _dnj −_ _P_ [ˇ] _nj_ ( _θ_ )] _znj_ = 0
_j_



for instruments _znj_ . As with its non-simulated analog, MSM is consistent if _znj_ is independent of [ _dnj −_ _P_ [ˇ] _nj_ ( _θ_ )].
The important feature of this estimator is that _P_ [ˇ] _nj_ ( _θ_ ) enters the
equation linearly. As a result, if _P_ [ˇ] _nj_ ( _θ_ ) is unbiased for _Pnj_ ( _θ_ ), then

[ _dnj −_ _P_ [ˇ] _nj_ ( _θ_ )] _znj_ is unbiased for [ _dnj −_ _Pnj_ ( _θ_ )] _znj_ . Since there is no
simulation bias in the estimation condition, the MSM estimator is
consistent, even when the number of draws _R_ is fixed. In contrast,
MSL contains simulation bias due to the log transformation of the
simulated probabilities. By not taking a non-linear transformation of
the simulated probabilities, MSM avoids simulation bias.
MSM still contains simulation noise (variance due to simulation).
This noise becomes smaller as _R_ rises and disappears when _R_ rises
without bound. As a result, MSM is asymptotically equivalent to
MOM if _R_ rises with _N_ .
Just like its unsimulated analog, MSM is less efficient than MSL
unless the ideal instruments are used. However, the ideal instruments
are functions of _lnPnj_ . They cannot be calculated exactly for any but
the simplest models, and, if they are simulated based on the simulated
probability, simulation bias is introduced by the log operation. MSM
is usually applied with non-ideal weights, which means that there is a
loss of efficiency. MSM with ideal weights that are simulated without
bias becomes MSS, which we discuss below.
In summary: MSM has the advantage over MSL of being consistent
with a fixed number of draws. However, there is no free lunch, and the
cost of this advantage is a loss of efficiency when non-ideal weights are
used.


**10.2.3** **Method of simulated scores: MSS**


MSS provides a possibility of attaining consistency without a loss of
efficiency. The cost of this double advantage is numerical: the versions
of MSS that provide efficiency have fairly poor numerical properties
such that calculation of the estimator can be difficult.
The method of scores is defined by the condition


     
_sn_ ( _θ_ ) = 0
_n_


278 _CHAPTER 10. SIMULATION-ASSISTED ESTIMATION_


where _sn_ ( _θ_ ) = _∂lnPn_ ( _θ_ ) _/∂θ_ is the score for observation _n_ . This is the
same defining condition as ML: when exact probabilities are used, the
method of scores is simply ML.
The method of simulated scores replaces the exact score with a
simulated counterpart. The MSS estimator is the value of _θ_ that solves

     
_s_ ˇ _n_ ( _θ_ ) = 0
_n_


where ˇ _sn_ ( _θ_ ) is a simulator of the score. If ˇ _sn_ ( _θ_ ) is calculated as
the derivative of the log of the simulated probability, i.e., ˇ _sn_ ( _θ_ ) =
_∂lnP_ [ˇ] _n_ ( _θ_ ) _/∂θ_, then MSS is the same as MSL. However, the score can
be simulated in other ways. When the score is simulated in other ways,
MSS differs from MSL and has different properties.
Suppose that an unbiased simulator of the score can be constructed.
With this simulator, the defining equation [�] _n_ _[s]_ [ˇ] _[n]_ [(] _[θ]_ [) = 0 does not]
incorporate any simulation bias, since the simulator enters the equation
linearly. MSS is therefore consistent with a fixed _R_ . The simulation
noise decreases as _R_ rises, such that MSS is asymptotically efficient,
equivalent to MSL, when _R_ rises with _N_ . In contrast, MSL uses the
biased score simulator ˇ _sn_ ( _θ_ ) = _∂lnP_ [ˇ] _n_ ( _θ_ ) _/∂θ_, which is biased due to
the log operator. MSS with an unbiased score simulator is therefore
better that MSL with its biased score simulator in two regards: it is
consistent under less stringent conditions (with fixed _R_ versus _R_ rising
with _N_ ) and is efficient under less stringent conditions ( _R_ rising at any
_√_
rate with _N_ versus _R_ rising faster than _N_ .)

The difficulty with MSS comes in finding an unbiased score simulator. The score can be rewritten as



_sn_ ( _θ_ ) = _[∂lnP][nj]_ [(] _[θ]_ [)]




_[nj]_ [(] _[θ]_ [)] 1 _∂Pnj_

=
_∂θ_ _Pnj_ ( _θ_ ) _∂θ_



_∂θ_ _[.]_



An unbiased simulator for the second term _∂Pnj/∂θ_ is easily obtained
by taking the derivative of the simulated probability. Since differentiation is a linear operation, _∂P_ [ˇ] _nj/∂θ_ is unbiased for _∂Pnj/∂θ_ if _P_ [ˇ] _nj_ ( _θ_ )
is unbiased for _Pnj_ ( _θ_ ). Since the second term in the score can be simulated without bias, the difficulty arises in finding an unbiased simulator
for the first term 1 _/Pnj_ ( _θ_ ). Of course, simply taking the inverse of the
simulated probability does not provide an unbiased simulator, since
1 _/ErP_ [ˇ] _nj_ ( _θ_ ) _̸_ = 1 _/Pnj_ ( _θ_ ). Like the log operation, an inverse introduces
bias.


_10.2. DEFINITION OF ESTIMATORS_ 279


One proposal is based on the recognition that 1 _/Pnj_ ( _θ_ ) is the expected number of draws of the random terms that are needed before an
“accept” is obtained. Consider drawing balls from an urn that contains
many balls of different colors. Suppose the probability of obtaining a
red ball is 0.20. That is, one-fifth of the balls are red. How many
draws would it take, on average, to obtain a red ball? The answer is
1/.2=5. The same idea can be applied to choice probabilities. _Pnj_ ( _θ_ )
is the probability that a draw of the random terms of the model will
result in alternative _j_ having the highest utility. The inverse 1 _/Pnj_ ( _θ_ )
can be simulated as follows:


1. Take a draw of the random terms from their density.


2. Calculate the utility of each alternative with this draw.


3. Determine whether alternative _j_ has the highest utility.


4. If so, call the draw an “accept.” If not, then call the draw a
“reject” and repeat steps 1 to 3 with a new draw. Define _B_ _[r]_ as
the number of draws that are taken until the first “accept” is
obtained.


5. Perform steps 1 to 4 _R_ times, obtaining _B_ _[r]_ for _r_ = 1 _, . . ., R_ . The
simulator of 1 _/Pnj_ ( _θ_ ) is (1 _/R_ ) [�] _[R]_ _r_ =1 _[B][r]_ [.]


This simulator is unbiased for 1 _/Pnj_ ( _θ_ ). The product of this simulator with the simulator _∂P_ [ˇ] _nj/∂θ_ provides an unbiased simulator of the
score. MSS based on this unbiased score simulator is consistent for
fixed _R_ and asymptotically efficient when _R_ rises with _N_ .
Unfortunately, the simulator of 1 _/Pnj_ ( _θ_ ) has the same difficulties as
the accept-reject simulators that we discussed in section (5.6). There is
no guarantee than an accept will be obtained within any given number
of draws. Also, the simulator is not continuous in parameters. The
discontinuity hinders the numerical procedures that are used to locate
the parameters that solve the MSS equation.
In summary, there are advantages and disadvantages of MSS relative to MSL, just as there are for MSM. Understanding the capabilities
of each estimator allows the researcher to make an informed choice
among them.


280 _CHAPTER 10. SIMULATION-ASSISTED ESTIMATION_

### **10.3 The central limit theorem**


Prior to deriving the properties of our estimators, it is useful to review
the central limit theorem. This theorem provides the basis for the
distributions of the estimators.
One of the most basic concepts in statistics is that, if we take
draws from a distribution with mean _µ_ and variance _σ_, the mean of
these draws will be normally distributed with mean _µ_ and variance
_σ/N_, where _N_ is a large number of draws. This concept is the central
limit theorem, stated intuitively rather than precisely. We will provide
a more complete and precise expression of these ideas.
Let _t_ = (1 _/N_ ) [�] _n_ _[t][n]_ [, where each] _[ t][n]_ [ is a draw a from a distribution]
with mean _µ_ and variance _σ_ . The realization of the draws are called
the sample, and _t_ is the sample mean. If we take a different sample
(i.e., obtain different values for the draws of each _tn_ ), then we will get
a different value for the statistic _t_ . Our goal is to derive the sampling
distribution of _t_ .
For most statistics, we cannot determine the sampling distribution
exactly for a given sample size. Instead, we examine how the sampling
distribution behaves as sample size rises without bound. A distinction
is made between the limiting distribution and the asymptotic distribution of a statistic. Suppose that, as sample size rises, the sampling
distribution of statistic _t_ converges to a fixed distribution. For example, the sampling distribution of _t_ might become arbitrarily close to a
normal with mean _t_ _[∗]_ and variance _σ_ . In this case, we say that _N_ ( _t_ _[∗]_ _, σ_ )
is the limiting distribution of _t_ and that _t_ converges in distribution to
_N_ ( _t_ _[∗]_ _, σ_ ). We denote this situation as _t_ _→_ _[d]_ _N_ ( _t_ _[∗]_ _, σ_ ).
In many cases, a statistic will not have a limiting distribution. As _N_
rises, the sampling distribution keeps changing. The mean of a sample
of draws is an example of a statistic without a limiting distribution. As
stated above, if _t_ is the mean of a sample of draws from a distribution
with mean _µ_ and variance _σ_, then _t_ is normally distributed with mean _µ_
and variance _σ/N_ . The variance decreases as _N_ rises. The distribution
changes as _N_ rises, becoming more and more tightly dispersed around
the mean. If a limiting distribution were to be defined in this case, it
would have to be the degenerate distribution at _µ_ : as _N_ rises without
bound, the distribution of _t_ collapses on _µ_ . This limiting distribution is
useless in understanding the variance of the statistic, since the variance
of this limiting distribution is zero. What do we do in this case to


_10.3. THE CENTRAL LIMIT THEOREM_ 281


understand the properties of the statistic?



If our original statistic does not have a limiting distribution, then
we often can transform the statistic in such a way that the transformed
statistic has a limiting distribution. Suppose, as in in our example of
a sample mean, that the statistic we are interested in does not have a
limiting distribution because its variance decreases as _N_ rises. In that
case, we can consider a transformation of the statistic that normalizes
_√_
for sample size. In particular, we can consider _N_ ( _t −_ _µ_ ). Suppose



for sample size. In particular, we can consider _N_ ( _t −_ _µ_ ). Suppose

that this statistic does indeed have a limiting distribution, for example
_√N_ ( _t −_ _µ_ ) _→d_ _N_ (0 _, σ_ ). In this case, we can derive the properties of

our original statistic from the limiting distribution of the transformed
statistic. Recall from basic principles of probabilities that, for fixed _a_
and _b_, if _a_ ( _t −_ _b_ ) is distributed normal with zero mean and variance _σ_,
then _t_ itself is distributed normal with mean _b_ and variance _σ/a_ [2] . This
concept can be applied to our limiting distribution. For large enough
_√_
_N_, _N_ ( _t −_ _µ_ ) is distributed approximately _N_ (0 _, σ_ ). Therefore, for



_N_, _N_ ( _t −_ _µ_ ) is distributed approximately _N_ (0 _, σ_ ). Therefore, for

large enough _N_, _t_ is distributed approximately _N_ ( _µ, σ/N_ ). We denote
this as _t_ _∼_ _[a]_ _N_ ( _µ, σ/N_ ). Note that this is not the limiting distribution
of _t_, since _t_ has no nondegenerate limiting distribution. Rather, it
is called the asymptotic distribution of _t_, derived from the limiting
_√_
distribution of _N_ ( _t −_ _µ_ ).



_N_ ( _t −_ _µ_ ).



We can now restate precisely our concepts about the sampling distribution of a sample mean. The central limit theorem states the following. Suppose _t_ is the mean of a sample of _N_ draws from a distribution with mean _µ_ and variance _σ_ . Then _√N_ ( _t −_ _µ_ ) _→d_ _N_ (0 _, σ_ ). With

this limiting distribution, we can say that _t_ _∼_ _[a]_ _N_ ( _µ, σ/N_ ).



There is another, more general version of the central limit theorem.
In the version just stated, each _tn_ is a draw from the same distribution.
Suppose _tn_ is a draw from a distribution with mean _µ_ and variance
_σn_, for _n_ = 1 _, . . ., N_ . That is, each _tn_ is from a different distribution;
the distributions have the same mean but different variances. The
_√_
generalized version of the central limit theorem states that _N_ ( _t −_

_µ_ ) _→_ _[d]_ _N_ (0 _, σ_ ), where _σ_ is now the average variance: _σ_ = (1 _/N_ ) [�] _n_ _[σ][n]_ [.]
Given this limiting distribution, we can say that _t_ _∼_ _[a]_ _N_ ( _µ, σ/N_ ). We
will use both versions of the central limit theorem when deriving the
distributions of our estimators.


282 _CHAPTER 10. SIMULATION-ASSISTED ESTIMATION_

### **10.4 Properties of traditional estimators**


In this section, we review the procedure for deriving the properties of
estimators and apply that procedure to the traditional, non-simulationbased estimators. This discussion provides the basis for analyzing the
properties of the simulation-based estimators in the next section.
The true value of the parameters is denoted _θ_ _[∗]_ . The ML and MOM
estimators are roots of an equation that takes the form


     
_gn_ ( _θ_ [ˆ] ) _/N_ = 0 _._ (10.2)
_n_


That is, the estimator _θ_ [ˆ] is the value of the parameters that solve this
equation. We divide by _N_, even though this division does not affect
the root of the equation, since doing so facilitates our derivation of
the properties of the estimators. The condition states that the average
value of _gn_ ( _θ_ ) in the sample is zero at the parameter estimates. For
moments of residuals with a vector of instruments,ML, _gn_ ( _θ_ ) is the score _∂lnPn_ ( _θ_ ) _/∂θ_ . For MOM, _gn_ ( _θ_ [�] ) is the set of first _j_ [(] _[d][nj][ −]_ _[P][nj]_ [)] _[z][nj]_ [.]
Equation (10.2) is often called the moment condition. In its nonsimulated form, the method of scores is the same as ML and therefore
need not be considered separately in this section. Note that we call
(10.2) an equation even though it is actually a set of equations, since
_gn_ ( _θ_ ) is a vector. The parameters that solve these equations are the
estimators.
At any particular value of _θ_, the mean and variance of _gn_ ( _θ_ ) can be
calculated for the sample. Label the mean as _g_ ( _θ_ ) and the variance as
_W_ ( _θ_ ). We are particularly interested in the sample mean and variance
of _gn_ ( _θ_ ) at the true parameters, _θ_ _[∗]_, since our goal is to estimate these
parameters.
The key to understanding the properties of an estimator comes in
realizing that each _gn_ ( _θ_ _[∗]_ ) is a draw from a distribution of _gn_ ( _θ_ _[∗]_ )’s in
the population. We do not know the true parameters, but we know
that each observation has a value of _gn_ ( _θ_ _[∗]_ ) at the true parameters. The
value of _gn_ ( _θ_ _[∗]_ ) varies over people in the population. So, by drawing
a person into our sample, we are essentially drawing a value of _gn_ ( _θ_ _[∗]_ )
from its distribution in the population.
The distribution of _gn_ ( _θ_ _[∗]_ ) in the population has a mean and variance. Label the mean of _gn_ ( _θ_ _[∗]_ ) in the population as **g** and its variance
in the population as **W** . The sample mean and variance at the true


_10.4. TRADITIONAL ESTIMATORS_ 283


parameters, _g_ ( _θ_ _[∗]_ ) and _W_ ( _θ_ _[∗]_ ), are the sample counterparts to the population mean and variance, **g** and **W** .
We assume that **g** = 0. That is, we assume that the average of
_gn_ ( _θ_ _[∗]_ ) in the population is zero at the true parameters. Under this
assumption, the estimator provides a sample analog to this population
expectation: _θ_ ˆ is the value of the parameters at which the sample
average of _gn_ ( _θ_ ) equals zero, as given in the defining condition 10.2.
For ML, the assumption that **g** = 0 simply states that the average
score in the population is zero, when evaluated at the true parameters.
In a sense, this can be considered the definition of the true parameters,
namely: _θ_ _[∗]_ are the parameters at which the log-likelihood function for
the entire population obtains its maximum and hence has zero slope.
The estimated parameters are the values that make the slope of the
likelihood function in the sample zero. For MOM, the assumption is
satisfied if the instruments are independent of the residuals. In a sense,
the assumption with MOM is simply a reiteration that the instruments
are exogenous. The estimated parameters are the values that make the
instruments and residuals uncorrelated in the sample.
We now consider the population variance of _gn_ ( _θ_ _[∗]_ ), which we have
denoted **W** . When _gn_ ( _θ_ ) is the score, as in ML, this variance takes a
special meaning. As shown in section (8.7), the information identity
states that **V** = _−_ **H** where








_−_ **H** = _−E_




_∂_ [2] _lnPn_ ( _θ_ _[∗]_ )

_∂θ∂θ_ _[′]_



is the information matrix and **V** is the variance of the scores evaluated
at the true parameters: **V** = _V ar_ ( _∂lnPn_ ( _θ_ _[∗]_ ) _/∂θ_ ). When _gn_ ( _θ_ ) is
the score, we have **W** = **V** by definition and hence **W** = _−_ **H** by
the information identity. That is, when _gn_ ( _θ_ ) is the score, **W** is the
information matrix. For MOM with non-ideal instruments, **W** _̸_ = _−_ **H**,
such that **W** does not equal the information matrix.
Why does this distinction matter? We will see that knowing whether
**W** equals the information matrix allows us to determine whether the
estimator is efficient. The lowest variance that any estimator can
achieve is _−_ **H** _[−]_ [1] _/N_ . For a proof, see, for example, Greene (2000) or
Ruud (2000). An estimator is efficient if its variance attains this lower
bound. As we will see, this lower bound is achieved when **W** = _−_ **H**
but not when **W** _̸_ = _−_ **H** .
Our goal is to determine the properties of _θ_ [ˆ] . We derive these prop

284 _CHAPTER 10. SIMULATION-ASSISTED ESTIMATION_


erties in a two-step process. First, we examine the distribution of _g_ ( _θ_ _[∗]_ ),
which, as stated above, is the sample mean of _gn_ ( _θ_ _[∗]_ ). Second, the distribution of _θ_ [ˆ] is derived from the distribution of _g_ ( _θ_ _[∗]_ ). This two step
process is not necessarily the most direct way of examining traditional
estimators. However, as we will see in the next section, it provides a
very convenient way for generalizing to simulation-based estimators.


**Step 1: The distribution of** _g_ ( _θ_ _[∗]_ ) **.**


Recall that the value of _gn_ ( _θ_ _[∗]_ ) varies over decision-makers in the population. When taking a sample, the researcher is drawing values of
_gn_ ( _θ_ _[∗]_ ) from its distribution in the population. This distribution has
zero mean by assumption and variance denoted **W** . The researcher
calculates the sample mean of these draws, _g_ ( _θ_ _[∗]_ ). By the central limit
theorem, _√N_ ( _g_ ( _θ_ _[∗]_ ) _−_ 0) _→d_ _N_ (0 _,_ **W** ) such that the sample mean has

distribution _g_ ( _θ_ _[∗]_ ) _∼_ _[a]_ _N_ (0 _,_ **W** _/N_ ).


**Step 2: Derive the distribution of** _θ_ [ˆ] **from the distribution of**
_g_ ( _θ_ _[∗]_ ) **.**


We can relate the estimator _θ_ [ˆ] to its defining term _g_ ( _θ_ ) as follows. Take
a first order Taylor’s expansion of _g_ ( _θ_ [ˆ] ) around _g_ ( _θ_ _[∗]_ ):


_g_ ( _θ_ [ˆ] ) = _g_ ( _θ_ _[∗]_ ) + _D_ [ _θ_ [ˆ] _−_ _θ_ _[∗]_ ] (10.3)


where _D_ = _∂g_ ( _θ_ _[∗]_ ) _/∂θ_ _[′]_ . By definition of _θ_ [ˆ] (that is, by defining condition
10.2), _g_ ( _θ_ [ˆ] ) = 0 so that the right-hand-side of this expansion is 0. Then:


0 = _g_ ( _θ_ _[∗]_ ) + _D_ [ _θ_ [ˆ] _−_ _θ_ _[∗]_ ]



( _θ_ [ˆ] _−_ _θ_ _[∗]_ ) = _−D_ _[−]_ [1] _g_ ( _θ_ _[∗]_ )
_√_ _√_



_√_
_N_ ( _θ_ [ˆ] _−_ _θ_ _[∗]_ ) =



_N_ ( _−D_ _[−]_ [1] ) _g_ ( _θ_ _[∗]_ ) _._ (10.4)



Denote the mean of _∂gn_ ( _θ_ _[∗]_ ) _/∂θ_ _[′]_ in the population as **D** . The sample mean of _∂gn_ ( _θ_ _[∗]_ ) _/∂θ_ _[′]_ is _D_, as defined above. The sample mean _D_
converges to the population mean **D** when sample size rises. We know
from step 1 that _√Ng_ ( _θ_ _[∗]_ ) _→d_ _N_ (0 _,_ **W** ). Using this fact in (10.4), we



from step 1 that _Ng_ ( _θ_ _[∗]_ ) _→d_ _N_ (0 _,_ **W** ). Using this fact in (10.4), we

have:
_√_



_N_ ( _θ_ [ˆ] _−_ _θ_ _[∗]_ ) _→_ _[d]_ _N_ (0 _,_ **D** _[−]_ [1] **WD** _[−]_ [1] ) _._ (10.5)



This limiting distribution tells us that _θ_ [ˆ] _∼_ _[a]_ _N_ ( _θ_ _[∗]_ _,_ **D** _[−]_ [1] **WD** _[−]_ [1] _/N_ ).


_10.5. SIMULATION-BASED ESTIMATORS_ 285


We can now observe the properties of the estimator. The asymptotic distribution of _θ_ [ˆ] is centered on the true value and its variance
decreases as sample size rises. As a result, _θ_ [ˆ] converges in probability
_p_
to _θ_ _[∗]_ as sample rise rises without bound: _θ_ [ˆ] _→_ _θ_ . The estimator is
therefore consistent. The estimator is asymptotically normal. And
its variance is **D** _[−]_ [1] **WD** _[−]_ [1] _/N_ which can be compared with the lowest
possible variance, _−_ **H** _[−]_ [1] _/N_, to determine whether it is efficient.
For ML, _gn_ ( _·_ ) is the score, such that the variance of _gn_ ( _θ_ _[∗]_ ) is the
variance of the scores: **W** = **V** . Also, the mean derivative of _gn_ ( _θ_ _[∗]_ )
is the mean derivative of the scores: **D** = **H** = _E_ ( _∂_ [2] _lnPn_ ( _θ_ _[∗]_ ) _/∂θ∂θ_ _[′]_ )
where the expectation is over the population. By the information identity, **V** = _−_ **H** . The asymptotic variance of _θ_ [ˆ] becomes **D** _[−]_ [1] **WD** _[−]_ [1] _/N_ =
**H** _[−]_ [1] **VH** _[−]_ [1] _/N_ = **H** _[−]_ [1] ( _−_ **H** ) **H** _[−]_ [1] _/N_ = _−_ **H** _[−]_ [1] _/N_, which is the lowest
possible variance of any estimator. ML is therefore efficient. Since
**V** = _−_ **H**, the variance of the ML estimator can also expressed as
**V** _[−]_ [1] _/N_, which has a readily interpretable meaning: the variance of
the estimator is equal to the variance of the scores evaluated at the
true parameters, divided by sample size.
For MOM, _gn_ ( _·_ ) is a set of moments. If the ideal instruments are
used, then MOM becomes ML and is efficient. If any other instruments are used, then MOM is not ML. In this case, **W** is the population variance of the moments and **D** is the mean derivatives of the
moments, rather than the variance and mean derivatives of the scores.
The asymptotic variance of _θ_ [ˆ] does not equal _−_ **H** _[−]_ [1] _/N_ . MOM without
ideal weights is therefore not efficient.

### **10.5 Properties of simulation-based estimators**


Suppose that the terms that enter the defining equation for an estimator are simulated rather than calculated exactly. Let ˇ _gn_ ( _θ_ ) denote the
simulated value of _gn_ ( _θ_ ) and ˇ _g_ ( _θ_ ) the sample mean of these simulated
values, such that ˇ _g_ ( _θ_ ) is the simulated version of _g_ ( _θ_ ). Denote the
number of draws used in simulation for each _n_ as _R_, and assume that
independent draws are used for each _n_ (e.g., separate draws are taken
for each _n_ .) Assume further that the same draws are used for each
value of _θ_ when calculating ˇ _gn_ ( _θ_ ). This procedure prevents “chatter”
in the simulation, such that the difference between ˇ _g_ ( _θ_ 1) and ˇ _g_ ( _θ_ 2) for
two different values of _θ_ is not due to different draws.
These assumptions on the simulation draws are easy for the re

286 _CHAPTER 10. SIMULATION-ASSISTED ESTIMATION_


searcher to implement and simplify our analysis considerably. For interested readers, Lee (1992) examines the situation when the same
draws are used for all observations. Pakes and Pollard (1989) provide
a way to characterize an equicontinuity condition that, when satisfied,
facilitates analysis of simulation-based estimators. McFadden (1989)
characterizes this condition in a different way and shows that it can be
met by using the same draws for each value of _θ_, which is the assumption that we make. McFadden (1996) provides a helpful synthesis that
includes a discussion of the need to prevent chatter.
The estimator is defined by the condition ˇ _g_ ( _θ_ [ˆ] ) = 0. We derive the
properties of _θ_ [ˆ] in the same two steps as for the traditional estimators.


**Step 1: The distribution of** ˇ _g_ ( _θ_ _[∗]_ ) **.**


To identify the various components of this distribution, let us reexpress ˇ _g_ ( _θ_ _[∗]_ ) by adding and subtracting some terms and rearranging:


_g_ ˇ( _θ_ _[∗]_ ) = _g_ ˇ( _θ_ _[∗]_ ) + _g_ ( _θ_ _[∗]_ ) _−_ _g_ ( _θ_ _[∗]_ ) + _Erg_ ˇ( _θ_ _[∗]_ ) _−_ _Erg_ ˇ( _θ_ _[∗]_ )

= _g_ ( _θ_ _[∗]_ ) + [ _Erg_ ˇ( _θ_ _[∗]_ ) _−_ _g_ ( _θ_ _[∗]_ )] + [ˇ _g_ ( _θ_ _[∗]_ ) _−_ _Erg_ ˇ( _θ_ _[∗]_ )]


where _g_ ( _θ_ _[∗]_ ) is the non-simulated value and _Erg_ ˇ( _θ_ _[∗]_ ) is the expectation
of the simulated value over the draws used in the simulation. Adding
and subtracting terms obviously does not change ˇ _g_ ( _θ_ _[∗]_ ). Yet, the subsequent rearrangement of the terms allows us to identify components
that have intuitive meaning.
The first term _g_ ( _θ_ _[∗]_ ) is the same as arises for the traditional estimator. The other two terms are extra elements that arise because of the
simulation. The term _Erg_ ˇ( _θ_ _[∗]_ ) _−_ _g_ ( _θ_ _[∗]_ ) captures the bias, if any, in the
simulator of _g_ ( _θ_ _[∗]_ ). It is the difference between the true value of _g_ ( _θ_ _[∗]_ )
and the expectation of the simulated value. If the simulator is unbiased for _g_ ( _θ_ _[∗]_ ), then _Erg_ ˇ( _θ_ _[∗]_ ) = _g_ ( _θ_ _[∗]_ ) and this term drops out. Often,
however, the simulator will not be unbiased for _g_ ( _θ_ _[∗]_ ). For example,
with MSL, ˇ _gn_ ( _θ_ ) = _∂lnP_ [ˇ] _n_ ( _θ_ ) _/∂θ_ where _P_ [ˇ] _n_ ( _θ_ ) is an unbiased simulator
of _Pn_ ( _θ_ ). Since _P_ [ˇ] _n_ ( _θ_ ) enters nonlinearly via the log operator, ˇ _gn_ ( _θ_ ) is
not unbiased. The third term, ˇ _g_ ( _θ_ _[∗]_ ) _−_ _Erg_ ˇ( _θ_ _[∗]_ ), captures simulation
noise, that is, the deviation of the simulator for given draws from its
expectation over all possible draws.
Combining these concepts, we have


_g_ ˇ( _θ_ ) = _A_ + _B_ + _C,_ (10.6)


_10.5. SIMULATION-BASED ESTIMATORS_ 287


where


_A_ is the same as in the traditional estimator,


_B_ is simulation bias,


_C_ is simulation noise.


To see how the simulation-based estimators differ from their traditional
counterparts, we examine the simulation bias _B_ and noise _C_ .
Consider first the noise. This term can be re-expressed as:


_C_ = _g_ ˇ( _θ_ _[∗]_ ) _−_ _Erg_ ˇ( _θ_ _[∗]_ )



1
=
_N_








 =



_g_ ˇ _n_ ( _θ_ _[∗]_ ) _−_ _Erg_ ˇ _n_ ( _θ_ _[∗]_ )
_n_



_dn/N_
_n_



where _dn_ is the deviation of the simulated value for observation _n_ from
its expectation. The key to understanding the behavior of the simulation noise comes in noting that _dn_ is simply a statistic for observation
_n_ . The sample constitutes _N_ draws of this statistic, one for each observation: _dn∀n_ = 1 _, . . ., N_ . The simulation noise _C_ is the average
of these _N_ draws. As such, the central limit theorem gives us the
distribution of _C_ .
In particular: For a given observation, the draws that are used
in simulation provide a particular value of _dn_ . If different draws had
been obtained, then a different value of _dn_ would have been obtained.
There is a distribution of values of _dn_ over the possible realizations of
the draws used in simulation. The distribution has zero mean, since
the expectation over draws is subtracted out when creating _dn_ . Label
the variance of the distribution as _Sn/R_, where _Sn_ is the variance when
one draw is used in simulation. There are two things to note about
this variance. First, _Sn/R_ is inversely related to _R_, the number of
draws that are used in simulation. Second, the variance is different for
different _n_ . Since _gn_ ( _θ_ _[∗]_ ) is different for different _n_, the variance of the
simulation deviation also differs.
We take a draw of _dn_ for each of _N_ observations; the overall simulation noise, _C_, is the average of these _N_ draws of observation-specific
simulation noise. As just stated, each _dn_ is a draw from a distribution
with zero mean and variance _Sn/R_ . The generalized version of the central limit theorem tells us the distribution of a sample average of draws


288 _CHAPTER 10. SIMULATION-ASSISTED ESTIMATION_


from distributions that have the same mean but different variances. In
our case,
_√_

_NC_ _→d_ _N_ (0 _,_ **S** _/R_ )


where **S** is the population mean of _Sn_ . Then _C_ _∼_ _[a]_ _N_ (0 _,_ **S** _/NR_ ).
The most relevant characteristic of the asymptotic distribution of
_C_ is that it decreases as _N_ increases, even when _R_ is fixed. Simulation noise disappears as sample size increases, even without increasing
the number of draws used in simulation. This is a very important
and powerful fact. It means that increasing the sample size is a way
to decrease the effects of simulation on the estimator. The result is
intuitively meaningful. Essentially, simulation noise cancels out over
observations. The simulation for one observation might, by chance,
make that observation’s ˇ _gn_ ( _θ_ ) too large. However, the simulation for
another observation is likely, by chance, to be too small. By averaging
the simulations over observations, the errors tend to cancel each other.
As sample size rises, this canceling out property becomes more powerful until, with large enough samples, simulation noise is negligible.
Consider now the bias. If the simulator ˇ _g_ ( _θ_ ) is unbiased for _g_ ( _θ_ ),
then the bias term _B_ in (10.6) is zero. However, if the simulator is
biased, as with MSL, then the effect of this bias on the distribution of
_g_ ˇ( _θ_ _[∗]_ ) must be considered.
Usually, the defining term _gn_ ( _θ_ ) is a function of a statistic, _ℓn_,
that can be simulated without bias. For example, with MSL, _gn_ ( _θ_ ) is
a function of the choice probability, which can be simulated without
bias; in this case _ℓn_ is the probability. More generally, _ℓn_ can be
any statistic that is simulated without bias and serves to define _gn_ ( _θ_ ).
We can write the dependence in general as _gn_ ( _θ_ ) = _g_ ( _ℓn_ ( _θ_ )) and the
unbiased simulator of _ℓn_ ( _θ_ ) as _ℓ_ [ˇ] _n_ ( _θ_ ) where _Erℓ_ [ˇ] _n_ ( _θ_ ) = _ℓn_ ( _θ_ ).
We can now re-express ˇ _gn_ ( _θ_ ) by taking a Taylor’s expansion around
the unsimulated value _gn_ ( _θ_ ):



_g_ ˇ _n_ ( _θ_ ) = _gn_ ( _θ_ ) + _[∂g]_ [(] _[ℓ][n]_ [(] _[θ]_ [))]




_[ℓ][n]_ [(] _[θ]_ [))]

[ _ℓ_ [ˇ] _n_ ( _θ_ ) _−_ _ℓn_ ( _θ_ )] + [1]
_∂ℓn_ 2



_∂_ [2] _g_ ( _ℓn_ ( _θ_ ))

[1]

2 _∂ℓ_ [2]



_n_ [ _ℓ_ [ˇ] _n_ ( _θ_ ) _−_ _ℓn_ ( _θ_ ] [2]

_∂ℓ_ [2] _n_



_g_ ˇ _n_ ( _θ_ ) _−_ _gn_ ( _θ_ ) = _gn_ _[′]_ [[ˇ] _[ℓ][n]_ [(] _[θ]_ [)] _[ −]_ _[ℓ][n]_ [(] _[θ]_ [)] +] [1] _n_ [[ˇ] _[ℓ][n]_ [(] _[θ]_ [)] _[ −]_ _[ℓ][n]_ [(] _[θ]_ [)]][2] _[.]_

2 _[g][′′]_



where _gn_ _[′]_ [and] _[ g]_ _n_ _[′′]_ [are simply shorthand ways to denote the first and]
second derivatives of _gn_ ( _ℓ_ ( _·_ )) with respect to _ℓ_ . Since _ℓ_ [ˇ] _n_ ( _θ_ ) is unbiased


_10.5. SIMULATION-BASED ESTIMATORS_ 289


for _ℓn_ ( _θ_ ), we know _Ergn_ _[′]_ [[ˇ] _[ℓ][n]_ [(] _[θ]_ [)] _[ −]_ _[ℓ][n]_ [(] _[θ]_ [)] =] _[ g]_ _n_ _[′]_ [[] _[E][r][ℓ]_ [ˇ] _[n]_ [(] _[θ]_ [)] _[ −]_ _[ℓ][n]_ [(] _[θ]_ [)] = 0. As]
a result, only the variance term remains in the expectation:


1
_Erg_ ˇ _n_ ( _θ_ ) _−_ _gn_ ( _θ_ ) = _n_ _[E][r]_ [[ˇ] _[ℓ][n]_ [(] _[θ]_ [)] _[ −]_ _[ℓ][n]_ [(] _[θ]_ [)]][2]
2 _[g][′′]_

1
= _n_ _[V ar][r][ℓ]_ [ˇ] _[n]_ [(] _[θ]_ [)] _[.]_
2 _[g][′′]_


Denote _V arrℓ_ [ˇ] _n_ ( _θ_ ) = _Qn/R_ to reflect the fact that the variance is
inversely proportional to the number of draws used in the simulation.
The simulation bias is then



1
_Erg_ ˇ( _θ_ ) _−_ _g_ ( _θ_ ) =
_N_


1
=
_N_

_Z_
=
_R_





_Erg_ ˇ _n_ ( _θ_ ) _−_ _gn_ ( _θ_ )
_n_

- _Qn_

_gn_ _[′′]_ 2 _R_
_n_



where _Z_ is the sample average of _gn_ _[′′][Q][n][/]_ [2.]
Since _B_ = _Z/R_, the value of this statistic normalized for sample
size is: _√_
_√_



_√_



_NB_ =



_N_
_R_ _[Z][.]_ (10.7)



_√_
If _R_ is fixed, then _B_ is non-zero. Even worse,



If _R_ is fixed, then _B_ is non-zero. Even worse, _NB_ rises with _N_,

such that it has no limiting value. Suppose that _R_ is considered to rise
_p_
with _N_ . The bias term then disappears asymptotically: _B_ = _Z/R_ _→_
0. However, the normalized bias term does not necessarily disappear.
_√_ _√_ _√_ _p_
Since _N_ enters the numerator of this term, _NB_ = ( _N/R_ ) _Z_ _→_ 0



_√_
_N_ enters the numerator of this term,



_√_
_NB_ = (



_p_

Since _N_ enters the numerator of this term, _NB_ = ( _N/R_ ) _Z_ _→_ 0

_√_ _√_
only if _R_ rises faster than _N_, such that the ratio _N/R_ approaches

_√_ _√_
zero as _N_ increases. If _R_ rises slower than _N_, the ratio _N/R_ rises,

such that the normalized bias term does not disappear but in fact gets
larger and larger as sample size increases.
We can now collect our results for the distribution of the defining
term normalized by sample size:
_√_ _√_



_√_
_N_, such that the ratio



_√_
_N_, the ratio



_√_
_N_ _g_ ˇ( _θ_ _[∗]_ ) =



_N_ ( _A_ + _B_ + _C_ ) _,_ (10.8)



where
_√_

_NA_ _→d_ _N_ (0 _,_ **W** ) _,_ the same as in the traditional estimator,


290 _CHAPTER 10. SIMULATION-ASSISTED ESTIMATION_



_√_



_NB_ =



_√_



_N_

_NB_ = _R_ _[Z][,]_ [ capturing simulation bias,]

_√_



_NC_ _→d_ _N_ (0 _,_ **S** _/R_ ) _,_ capturing simulation noise.



**Step 2: Derive distribution of** _θ_ [ˆ] **from distribution of** ˇ _g_ ( _θ_ _[∗]_ ) **.**



As with the traditional estimators, the distribution of _θ_ [ˆ] is directly
related to the distribution of ˇ _g_ ( _θ_ _[∗]_ ). Using the same Taylor’s expansion
as in (10.3), we have
_√_ _[√]_ _[√]_



_N_ ( _θ_ [ˆ] _−_ _θ_ _[∗]_ ) = _−D_ [ˇ] _[−]_ [1] _[√]_



_N_ _g_ ˇ( _θ_ _[∗]_ ) = _−D_ [ˇ] _[−]_ [1] _[√]_



_N_ ( _A_ + _B_ + _C_ )(10.9)



where _D_ [ˇ] is the derivative of ˇ _g_ ( _θ_ _[∗]_ ) with respect to the parameters, which
converges to its expectation **D** [ˇ] as sample size rises. The estimator itself
is expressed as
_θ_ ˆ = _θ_ _[∗]_ _−_ _D_ ˇ _[−]_ [1] ( _A_ + _B_ + _C_ ) (10.10)


We can now examine the properties of our estimators.


**10.5.1** **Maximum simulated likelihood**



_√_ For MSL, ˇ _√gn_ ( _θ_ ) is not unbiased for _gn_ ( _θ_ ). The bias term in (10.9) is

_NB_ = ( _N/R_ ) _Z_ . Suppose _R_ rises with _N_ . If _R_ rises faster than

_√_



_√_
_NB_ = (



_N_, then _√_



_√_
_NB_ = (



_p_
_N/R_ ) _Z_ _→_ 0 _,_



_√_
since the ratio



since the ratio _N/R_ falls to zero. Consider now the third term in

(10.9), which captures simulation noise: _√NC_ _→d_ _N_ (0 _,_ **S** _/R_ ). Since



(10.9), which captures simulation noise: _NC_ _→d_ _N_ (0 _,_ **S** _/R_ ). Since

_p_
**S** _/R_ decreases as _R_ rises, we have **S** _/R_ _→_ 0 as _N →∞_ when _R_ rises
with _N_ . The second and third terms disappear, leaving only the first
term. This first term is the same as appears for the non-simulated
estimator. We have:
_√_ _[√]_



_N_ ( _θ_ [ˆ] _−_ _θ_ _[∗]_ ) = _−_ **D** _[−]_ [1] _[√]_



_NA_ _→d_ _N_ (0 _,_ **D** _[−]_ [1] **WD** _[−]_ [1] )



= _N_ (0 _,_ **H** _[−]_ [1] **VH** _[−]_ [1] )

= _N_ (0 _, −_ **H** _[−]_ [1] )


where the next to last equality occurs because _gn_ ( _θ_ ) is the score, and
the last equality is due to the information identity. The estimator is
distributed
_θ_ ˆ _∼_ _[a]_ _N_ ( _θ_ _[∗]_ _, −_ **H** _[−]_ [1] _/N_ ) _._


