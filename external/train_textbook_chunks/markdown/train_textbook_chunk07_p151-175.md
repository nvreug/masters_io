_5.6. SIMULATION OF THE CHOICE PROBABILITIES_ 141


The probability of alternative 1 is _Pn_ 1 = _Prob_ ( _U_ [˜] _n_ 21 _<_ 0 and _U_ [˜] _n_ 31 _<_
0) = _Prob_ ( _V_ [˜] _n_ 21 + ˜ _εn_ 21 _<_ 0 and _V_ [˜] _n_ 31 + ˜ _εn_ 31 _<_ 0). This probability is
hard to evaluate numerically in terms of the ˜ _ε_ ’s because they are correlated. However, using the transformation based on the Choleski factor,
the probability can be written in a way that involves independent random terms. The probability becomes a function of the one dimensional
standard cumulative normal distribution:


_Pn_ 1 = _Prob_ ( _V_ [˜] _n_ 21 + _caaη_ 1 _<_ 0 and _V_ [˜] _n_ 31 + _cabη_ 1 + _cbbη_ 2 _<_ 0)

= _Prob_ ( _V_ [˜] _n_ 21 + _caaη_ 1 _<_ 0) _× Prob_ ( _V_ [˜] _n_ 31 + _cabη_ 1 + _cbbη_ 2 _<_ 0 _|_ _V_ [˜] _n_ 21 + _caaη_ 1 _<_ 0)



= _Prob_ ( _η_ 1 _< −V_ [˜] _n_ 21 _/caa_ ) _× Prob_ ( _η_ 2 _< −_ ( _V_ [˜] _n_ 31 + _cabη_ 1) _/cbb | η_ 1 _< −V_ [˜] _n_ 21 _/caa_ )




         - _−V_ ˜ _n_ 21 _/caa_
= Φ( _−V_ [˜] _n_ 21 _/caa_ ) _×_



Φ( _−_ ( _V_ [˜] _n_ 31 + _cabη_ 1) _/cbb_ ) _φ_ ( _η_ 1) _dη_ 1
_η_ 1= _−∞_



where Φ( _·_ ) is the standard normal cumulative distribution evaluated
at the point in the parentheses and _φ_ ( _·_ ) is the standard normal density. The first term, Φ( _−V_ [˜] _n_ 21 _/caa_ ) is easy to calculate: it is simply
the cumulative standard normal evaluated at _−V_ [˜] _n_ 21 _/caa_ . Computer
packages contain fast routines for calculating the cumulative standard
normal. The second term is an integral. As we know, computers cannot integrate, and we use simulation to approximate integrals. This is
the heart of the GHK procedure: using simulation to approximate the
integral in the second term in _Pn_ 1.
Let us examine this integral more closely. It is the integral over
a truncated normal, namely, over _η_ 1 up to _−V_ [˜] _n_ 21 _/caa_ . The simulation proceeds as follows. Draw a value of _η_ 1 from a standard normal
density truncated above at _−V_ [˜] _n_ 21 _/caa_ . For this draw, calculate the
term Φ( _−_ ( _V_ [˜] _n_ 31 + _cabη_ 1) _/cbb_ ). Repeat this process for many draws,
and average the results. This average is a simulated approximation
to - _η−_ 1= _V_ ˜ _n−∞_ 21 _/caa_ Φ( _−_ ( _V_ [˜] _n_ 31 + _cabη_ 1) _/cbb_ ) _φ_ ( _η_ 1) _dη_ 1. The simulated probability is then obtained by multiplying this average by the value of
Φ( _−V_ [˜] _n_ 21 _/caa_ ), which is calculated exactly. Simple enough!
The question arises: how do we take a draw from a truncated
normal? We describe how to take draws from truncated univariate
distributions in section (9.2.4). The reader might want to jump ahead
and quickly review that section. For truncated normals, the process
is: Take a draw from a standard uniform, labeled _µ_ . Then calculate
_η_ = Φ _[−]_ [1] ( _µ_ Φ( _−V_ [˜] _n_ 21 _/caa_ )). The resulting _η_ is a draw from a normal
density truncated from above at _−V_ [˜] _n_ 21 _/caa_ .


142 _CHAPTER 5. PROBIT_


We can now put this all together to give the explicit steps that
are used for the GHK simulator in our three-alternative case. The
probability of alternative 1 is:


           - _−V_ ˜ _n_ 21 _/caa_
_Pn_ 1 = Φ( _−V_ [˜] _n_ 21 _/caa_ ) _×_ Φ( _−_ ( _V_ [˜] _n_ 31 + _cabη_ 1) _/cbb_ ) _φ_ ( _η_ 1) _dη_ 1 _._

_η_ 1= _−∞_


This probability is simulated as follows:


1. Calculate _k_ = Φ( _−V_ [˜] _n_ 21 _/caa_ ).


2. Draw a value of _η_ 1, labeled _η_ 1 _[r]_ [, from a truncated standard normal]
truncated at _−V_ [˜] _n_ 21 _/caa_ . This is accomplished as follows:


(a) Draw a standard uniform _µ_ _[r]_ .

(b) Calculate _η_ 1 _[r]_ [= Φ] _[−]_ [1][(] _[µ][r]_ [Φ(] _[−][V]_ [˜] _[n]_ [21] _[/c][aa]_ [).]

3. Calculate _g_ _[r]_ = Φ( _−_ ( _V_ [˜] _n_ 31 + _cabη_ 1 _[r]_ [)] _[/c][bb]_ [).]

4. The simulated probability for this draw is _P_ [ˇ] _n_ _[r]_ 1 [=] _[ k][ ×][ g][r]_ [.]


5. Repeat steps 1-4 _R_ times and average the results. This average
is the simulated probability: _P_ [ˇ] _n_ 1 = (1 _/R_ ) [�] _P_ [ˇ] _n_ _[r]_ 1 [.]


A graphical depiction is perhaps useful. Figure 5.3 shows the probability for alternative 1 in the space of independent errors _η_ 1 and _η_ 2.
The x-axis is the value of _η_ 1, and the y-axis is the value of _η_ 2. The line
labeled _A_ is where _η_ 1 is equal to _−V_ [˜] _n_ 21 _/caa_ . The condition that _η_ 1 is
below _−V_ [˜] _n_ 21 _/caa_ is met in the striped area to the left of line A. The line
labeled _B_ is where _η_ 2 = _−_ ( _V_ [˜] _n_ 31 + _cbaη_ 1) _/cbb_ . Note that the y-intercept
is where _η_ 1 = 0 such that _η_ 2 = _−V_ [˜] _n_ 31 _/cbb_ at this point. The slope of
the line is _−cba/cbb_ . The condition that _η_ 2 _< −_ ( _V_ [˜] _n_ 31 + _cbaη_ 1) _/cbb_ is
satisfied below line _B_ . The shaded area is where _η_ 1 is to the left of
line _A_ and _η_ 2 is below line _B_ . The mass of density in the shaded area
is therefore the probability that alternative 1 is chosen.
The probability (i.e., the shaded mass) is the mass of the striped
area times the proportion of this striped mass that is below line B.
The striped area has mass Φ( _−V_ [˜] _n_ 21 _/caa_ ). This is easy to calculate.
For any given value of _η_ 1, the portion of the striped mass that is below
line B is also easy to calculate. For example, in Figure 5.4, when
_η_ 1 takes the value _η_ 1 _[r]_ [, then the probability that] _[ η]_ [2][ is below line B is]
the share of line C’s mass that is below line B. This share is simply


_5.6. SIMULATION OF THE CHOICE PROBABILITIES_ 143


Figure 5.3: Probability of alternative 1.


Φ( _−_ ( _V_ [˜] _n_ 31 + _cabη_ 1 _[r]_ [)] _[/c][bb]_ [). The portion of the striped mass that is below]
line B is therefore the average of Φ( _−_ ( _V_ [˜] _n_ 31 + _cabη_ 1 _[r]_ [)] _[/c][bb]_ [) over all values]
of _η_ 1 that are to the left of line A. This average is simulated by taking
draws of _η_ 1 to the left of line A, calculating Φ( _−_ ( _V_ [˜] _n_ 31 + _cabη_ 1 _[r]_ [)] _[/c][bb]_ [)]
for each draw, and averaging the results. The probability is then this
average times the mass of the striped area, Φ( _−V_ [˜] _n_ 21 _/caa_ ).


**General model**


We can now describe the GHK simulator in general terms quickly, since
the basic logic has already been discussed. This succinct expression
serves to reinforce the concept that the GHK simulator is actually
easier than it might at first appear.
Utility is expressed as:


_Unj_ = _Vnj_ + _εnj_ _j_ = 1 _, ..., J_


_εn_ = _< εn_ 1 _, ..., εnJ >_ _εn_ : _J ×_ 1

_εn ∼_ _N_ (0 _,_ Ω)


Transform to utility differences against alternative _i_ :


_U_ ˜ _nji_ = ˜ _Vnji_ + ˜ _εnji,_ _j ̸_ = _i_



![](/Users/nicholasvreugdenhil/ASU Dropbox/Nicholas Vreugdenhil/masters_io_2026/external/train_textbook_chunks/markdown/train_textbook_chunk07_p151-175_images/train_textbook_chunk07_p151-175.pdf-2-0.png)

![](/Users/nicholasvreugdenhil/ASU Dropbox/Nicholas Vreugdenhil/masters_io_2026/external/train_textbook_chunks/markdown/train_textbook_chunk07_p151-175_images/train_textbook_chunk07_p151-175.pdf-2-1.png)

![](/Users/nicholasvreugdenhil/ASU Dropbox/Nicholas Vreugdenhil/masters_io_2026/external/train_textbook_chunks/markdown/train_textbook_chunk07_p151-175_images/train_textbook_chunk07_p151-175.pdf-2-2.png)

![](/Users/nicholasvreugdenhil/ASU Dropbox/Nicholas Vreugdenhil/masters_io_2026/external/train_textbook_chunks/markdown/train_textbook_chunk07_p151-175_images/train_textbook_chunk07_p151-175.pdf-2-3.png)

![](/Users/nicholasvreugdenhil/ASU Dropbox/Nicholas Vreugdenhil/masters_io_2026/external/train_textbook_chunks/markdown/train_textbook_chunk07_p151-175_images/train_textbook_chunk07_p151-175.pdf-2-4.png)

![](/Users/nicholasvreugdenhil/ASU Dropbox/Nicholas Vreugdenhil/masters_io_2026/external/train_textbook_chunks/markdown/train_textbook_chunk07_p151-175_images/train_textbook_chunk07_p151-175.pdf-2-5.png)

![](/Users/nicholasvreugdenhil/ASU Dropbox/Nicholas Vreugdenhil/masters_io_2026/external/train_textbook_chunks/markdown/train_textbook_chunk07_p151-175_images/train_textbook_chunk07_p151-175.pdf-2-6.png)

![](/Users/nicholasvreugdenhil/ASU Dropbox/Nicholas Vreugdenhil/masters_io_2026/external/train_textbook_chunks/markdown/train_textbook_chunk07_p151-175_images/train_textbook_chunk07_p151-175.pdf-2-7.png)

![](/Users/nicholasvreugdenhil/ASU Dropbox/Nicholas Vreugdenhil/masters_io_2026/external/train_textbook_chunks/markdown/train_textbook_chunk07_p151-175_images/train_textbook_chunk07_p151-175.pdf-2-8.png)
144 _CHAPTER 5. PROBIT_


Figure 5.4: Probability that _η_ 2 is in the correct range given _η_ 1 _[r]_ [.]



![](/Users/nicholasvreugdenhil/ASU Dropbox/Nicholas Vreugdenhil/masters_io_2026/external/train_textbook_chunks/markdown/train_textbook_chunk07_p151-175_images/train_textbook_chunk07_p151-175.pdf-3-0.png)
_5.6. SIMULATION OF THE CHOICE PROBABILITIES_ 145


_ε_ ˜ _ni_ = _<_ ˜ _εn_ 1 _, ...,_ ˜ _εnJ >_ where ... is over all except _i_


_ε_ ˜ _ni_ : ( _J −_ 1) _×_ 1

_ε_ ˜ _ni ∼_ _N_ (0 _,_ Ω [˜] _i_ )

where Ω [˜] _i_ is derived from Ω.
Re-express the errors as a Choleski transformation of iid standard
normal deviates
_Li_ s.t. _LiL_ _[′]_ _i_ [= Ω] _[i]_



_c_ 11 0 _. . ._ _. . ._ _. . ._ 0
_c_ 21 _c_ 22 0 _. . ._ _. . ._ 0
_c_ 31 _c_ 32 _c_ 33 0 _. . ._ 0
... _·_














_Li_ =














Then stacking utilities _U_ [˜] _ni_ = ( _U_ [˜] _n_ 1 _i, ...,_ _U_ [˜] _nJi_ ), we get the vector form of
the model
_U_ ˜ _ni_ = ˜ _Vni_ + _Liηn_


where _ηn_ = _< η_ 1 _n, ..., ηJ−_ 1 _,n >_ is a vector of iid standard normal deviates: _ηnj ∼_ _N_ (0 _,_ 1) _∀_ _j_ . Written explicitly the model is


_U_ ˜ _n_ 1 = ˜ _Vn_ 1 + _c_ 11 _η_ 1


_U_ ˜ _n_ 2 = ˜ _Vn_ 2 + _c_ 21 _η_ 1 + _c_ 22 _η_ 2
_U_ ˜ _n_ 3 = ˜ _Vn_ 3 + _c_ 31 _η_ 1 + _c_ 32 _η_ 2 + _c_ 33 _η_ 3


and so on. The choice probabilities are



_Pni_ = _Prob_ ( _U_ [˜] _nji <_ 0 _∀_ _j ̸_ = _i_ )











= _Prob_


_×_ _Prob_


_×_ _Prob_



_η_ 1 _<_ _[−][V]_ [˜] _[n]_ [1] _[i]_



_η_ 3 _<_ _[−]_ [( ] _[V]_ [˜] _[n]_ [3] _[i]_ [ +] _[ c]_ [31] _[η]_ [1][ +] _[ c]_ [32] _[η]_ [2][)]







_c_ 11



_η_ 2 _<_ _[−]_ [( ] _[V]_ [˜] _[n]_ [2] _[i]_ [ +] _[ c]_ [21] _[η]_ [1][)]



_c_ 11












_[i]_ [ +] _[ c]_ [21] _[η]_ [1][)]

_| η_ 1 _<_ _[−][V]_ [˜] _[n]_ [1] _[i]_
_c_ 22 _c_ 11




[31] _[η]_ [1][ +] _[ c]_ [32] _[η]_ [2][)]

_| η_ 1 _<_ _[−][V]_ [˜] _[n]_ [1] _[i]_
_c_ 33 _c_ 11




_[V]_ [˜] _[n]_ [1] _[i]_

and _η_ 2 _<_ _[−]_ [( ] _[V]_ [˜] _[n]_ [2] _[i]_ [ +] _[ c]_ [21] _[η]_ [1][)]
_c_ 11 _c_ 22



_c_ 22







_×_ and so on


The GHK simulator is calculated as follows:


146 _CHAPTER 5. PROBIT_



1. Calculate
















_−V_ [˜] _n_ 1 _i_

_c_ 11



_Prob_



_η_ 1 _<_ _[−][V]_ [˜] _[n]_ [1] _[i]_



_c_ 11



= Φ



2. Draw a value of _η_ 1, labeled _η_ 1 _[r]_ [, from a truncated standard normal]
truncated at _−V_ [˜] 1 _in/c_ 11.This draw is obtained as follows:


(a) Draw a standard uniform _µ_ _[r]_ 1
(b) Calculate _η_ 1 _[r]_ [= Φ] _[−]_ [1][(] _[µ]_ 1 _[r]_ [Φ(] _[−][V]_ [˜] _[n]_ [1] _[i][/c]_ [11][))]


3. Calculate















_Prob_



_η_ 2 _<_ _[−]_ [( ] _[V]_ [˜] _[n]_ [2] _[i]_ [ +] _[ c]_ [21] _[η]_ [1][)] _| η_ 1 = _η_ 1 _[r]_

_c_ 22



_η_ 2 _<_ _[−]_ [( ] _[V]_ [˜] _[n]_ [2] _[i]_ [ +] _[ c]_ [21] _[η]_ [1][)]



= Φ





_−_ ( _V_ [˜] _n_ 2 _i_ + _c_ 21 _η_ 1 _[r]_ [)]
_c_ 22



4. Draw a value of _η_ 2, labeled _η_ 2 _[r]_ [, from a truncated standard nor-]
mal truncated at _−_ ( _V_ [˜] _n_ 2 _i_ + _c_ 21 _η_ 1 _[r]_ [)] _[/c]_ [22][. This draw is obtained as]
follows:


(a) Draw a standard uniform _µ_ _[r]_ 1
(b) Calculate _η_ 2 _[r]_ [= Φ] _[−]_ [1][(] _[µ]_ 2 _[r]_ [Φ(] _[−]_ [( ˜] _[V][n]_ [2] _[i]_ [ +] _[ c]_ [21] _[η]_ 1 _[r]_ [)] _[/c]_ [22][))]


5. Calculate

















_−_ ( _V_ [˜] _n_ 3 _i_ + _c_ 31 _η_ 1 _[r]_ [+] _[ c]_ [32] _[η]_ 2 _[r]_ [)]
_c_ 33



_Prob_



_η_ 3 _<_ _[−]_ [( ] _[V]_ [˜] _[n]_ [3] _[i]_ [ +] _[ c]_ [31] _[η]_ [1][ +] _[ c]_ [32] _[η]_ [2][)] _| η_ 1 = _η_ 1 _[r]_ _[, η]_ [2] [=] _[ η]_ 2 _[r]_

_c_ 33



_η_ 3 _<_ _[−]_ [( ] _[V]_ [˜] _[n]_ [3] _[i]_ [ +] _[ c]_ [31] _[η]_ [1][ +] _[ c]_ [32] _[η]_ [2][)]



= Φ



6. And so on for all alternatives but _i_ .


7. The simulated probability for this _r_ _[th]_ draw of _η_ 1 _, η_ 2 _, ..._ is calculated as







_P_ ˇ _ni_ _[r]_ = Φ


_×_ Φ


_×_ Φ




_−V_ [˜] _n_ 1 _i_





_−_ ( _V_ [˜] _n_ 3 _i_ + _c_ 31 _η_ 1 _[r]_ [+] _[ c]_ [32] _[η]_ 2 _[r]_ [)]
_c_ 33



_c_ 11





_−_ ( _V_ [˜] _n_ 2 _i_ + _c_ 21 _η_ 1 _[r]_ [)]
_c_ 22











_×_ etc.


8. Repeat steps 1–7 many times, for _r_ = 1 _, ..., R_ .


_5.6. SIMULATION OF THE CHOICE PROBABILITIES_ 147


9. The simulated probability is



_P_ ˇ _in_ = [1]

_R_





_P_ ˇ _in_ _[r]_ _[.]_
_r_



**GHK simulator with maximum likelihood estimation**



There are several issues that need to be addressed when using the
GHK simulator in maximum likelihood estimation. First, in the loglikelihood function, we use the probability of the decision-maker’s chosen alternative. Since different decision-makers choose different alternatives, _Pni_ must be calculated for different _i_ ’s. The GHK simulator
takes utility differences against the alternative for which the probability is being calculated, and so different utility differences must be taken
for decision-makers who chose different alternatives. Second, for a person who chose alternative _i_, the GHK simulator uses the covariance
matrix Ω [˜] _i_, while for a person who chose alternative _j_, the matrix Ω [˜] _j_ is
used. Both of these matrices are derived from the same covariance matrix Ωof the original errors. We must assure that the parameters in Ω [˜] _i_
are consistent with those in Ω [˜] _j_, in the sense that they both are derived
from a common Ω. Third, we need to assure that the parameters that
are estimated by maximum likelihood imply covariance matrices Ω _j ∀_ _j_
that are positive definite, as a covariance matrix must be. Fourth, as
always, we must make sure that the model is normalized for scale and
level of utility, so that the parameters are identified.
Researchers use various procedures to address these issues. I will
describe the procedure that I use.
To assure that the model is identified, I start with the covariance
matrix of scaled utility differences with the differences taken against
the first alternative. This is matrix Ω [˜] 1 which is ( _J −_ 1) _×_ ( _J −_ 1). To
assure that the covariance matrix is positive definite, I parameterize
the model in terms of the Choleski factor of Ω [˜] 1. That is, I start with a
lower-triangular matrix that is ( _J −_ 1) _×_ ( _J −_ 1) whose top-left element
is 1:  



1 0 _. . ._ _. . ._ _. . ._ 0
_c_ 21 _c_ 22 0 _. . ._ _. . ._ 0
_c_ 31 _c_ 32 _c_ 33 0 _. . ._ 0
... _·_














_L_ 1 =














The elements _ckℓ_ of this Choleski factor are the parameters that are
estimated in the model. Any matrix that is the product of a lower

148 _CHAPTER 5. PROBIT_



triangular full-rank matrix multiplied by itself is positive definite. So
by using the elements of _L_ 1 as the parameters, I am assured that Ω [˜] 1
is positive definite for any estimated values of these parameters.
The matrix Ωfor the _J_ non-differenced errors is created from _L_ 1.
I create a _J × J_ Choleski factor for Ωby adding a row of zeros at the
top of _L_ 1 and a column of zeros at the left. The resulting matrix is



0 0 _. . ._ _. . ._ _. . ._ _. . ._ 0
0 1 0 _. . ._ _. . ._ _. . ._ 0
0 _c_ 21 _c_ 22 0 _. . ._ _. . ._ 0
0 _c_ 31 _c_ 32 _c_ 33 0 _. . ._ 0

0 ... _· · ·_







 _._









_L_ =
















Then Ωis calculated as _LL_ _[′]_ . With this Ω, I can derive Ω [˜] _j_ for any
_j_ . Note that Ωconstructed in this way is fully general (i.e., allows
any substitution pattern), since it utilizes all the parameters in the
normalized Ω [˜] 1.
Utility is expressed in vector form stacked by alternatives: _Un_ =
_Vn_ + _εn_, _εn ∼_ _N_ (0 _,_ Ω). Consider a person who has chosen alternative
_i_ . For the log-likelihood function, we want to calculate _Pni_ . Recall the
matrix _Mi_ that we introduced in section (5.1). Utility differences are
taken using this matrix: _U_ [˜] _ni_ = _MiUn,_ _V_ [˜] _ni_ = _MiVn_, and ˜ _εni_ = _Miεn_ .
The covariance of the error differences ˜ _εni_ is calculated as Ω [˜] _i_ = _Mi_ Ω _Mi_ _[′]_ [.]
The Choleski factor of Ω [˜] _i_ is taken and labeled _Li_ . (Note that _L_ 1
obtained here will necessarily be the same as the _L_ 1 that we used
at the beginning to parameterize the model.) The person’s utility
is expressed as: _U_ ˜ _ni_ = ˜ _Vni_ + _Liηn_ where _ηn_ is a ( _J −_ 1) vector of
iid standard normal deviates. The GHK simulator is applied to this
expression.
This procedure satisfies all of our requirements. The model is necessarily normalized for scale and level since we parameterize the model
in terms of the Choleski factor _L_ 1 of the covariance of _scaled_ error
_differences_, Ω [˜] 1. Each Ω [˜] _i_ is consistent with each other Ω [˜] _j_ for _j ̸_ = _i_,
because they are both derived from the same Ω(which is constructed
from _L_ 1.) Each Ω [˜] _i_ is positive definite for any values of the parameters,
because the parameters are the elements of _L_ 1. As stated above, any
matrix that is the product of a lower triangular matrix multiplied by
itself is positive definite, and so Ω [˜] 1 = _LL_ _[′]_ is positive definite. And each
of the other Ω [˜] _j_ ’s, for _j_ = 2 _, . . ., J_, is also positive definite, since they
are constructed to be consistent with Ω1, which is positive definite.


_5.6. SIMULATION OF THE CHOICE PROBABILITIES_ 149


**GHK as importance sampling**


As I described above in the three-alternative case, the GHK simulator
provides a simulated approximation of the integral


      - _−V_ ˜ _n_ 21 _/caa_

Φ( _−_ ( _V_ [˜] _n_ 31 + _cabη_ 1) _/cbb_ ) _φ_ ( _η_ 1) _dη_ 1 _._
_η_ 1= _−∞_


The GHK simulator can be interpreted in another way that is often
useful.
Importance sampling is a way of transforming an integral to be
more convenient to simulate. The procedure is described in section
(9.2.7), and readers might find it useful to jump ahead to review that
section. Importance sampling can be summarized following. Consider

        any integral _t_ [¯] = _t_ ( _ε_ ) _g_ ( _ε_ ) _dε_ over density _g_ . Suppose that another density exists from which it is easy to draw. Label this other density _f_ ( _ε_ ).
The density _g_ is called the target density and _f_ is the generating den
                     sity. The integral can be rewritten as _t_ [¯] = [ _t_ ( _ε_ ) _g_ ( _ε_ ) _/f_ ( _ε_ )] _f_ ( _ε_ ) _dε_ . This
integral is simulated by taking draws from _f_, calculating [ _t_ ( _ε_ ) _g_ ( _ε_ ) _/f_ ( _ε_ )]
for each draw, and averaging the results. This procedure is called importance sampling because each draw from _f_ is weighted by _g/f_ when
taking the average of _t_ ; the weight _g/f_ is the “importance” of the draw
from _f_ . This procedure is advantageous if (1) it is easier to draw from
_f_ than _g_, and/or (2) the simulator based on [ _t_ ( _ε_ ) _g_ ( _ε_ ) _/f_ ( _ε_ )] has better
properties (e.g., smoothness) than the simulator based on _t_ ( _ε_ ).
The GHK simulator can be seen as making this type of transformation, and hence as being a type of importance sampling. Let _η_ be
a vector of _J −_ 1 iid standard normal deviates. The choice probability
can be expressed as

             _Pni_ = _I_ ( _η ∈_ _B_ ) _g_ ( _η_ ) _dη_ (5.7)


where _B_ = _{η_ s.t _U_ ˜ _nji <_ 0 _∀_ _j ̸_ = _i}_ is the set of _η_ ’s that result in
_i_ being chosen; _g_ ( _η_ ) = _φ_ ( _η_ 1) _...φ_ ( _ηJ−_ 1) is the density where _φ_ denotes
the standard normal density; and utilities are:


_U_ ˜ _n_ 1 = ˜ _Vn_ 1 + _c_ 11 _η_ 1


_U_ ˜ _n_ 2 = ˜ _Vn_ 2 + _c_ 21 _η_ 1 + _c_ 22 _η_ 2
_U_ ˜ _n_ 3 = ˜ _Vn_ 3 + _c_ 31 _η_ 1 + _c_ 32 _η_ 2 + _c_ 33 _η_ 3


150 _CHAPTER 5. PROBIT_



etc.
The direct way to simulate this probability is to take draws of _η_,
calculate _I_ ( _η ∈_ _B_ ) for each draw and average the results. This is the
A-R simulator. This simulator has the unfortunate properties that it
can be zero and is not smooth.
For GHK we draw _η_ from a different density, not from _g_ ( _η_ ). Recall
that for GHK, we draw _η_ 1 from a standard normal density truncated at
_−V_ [˜] _n_ 1 _i/c_ 11. The density of this truncated normal is Φ( _−φV_ ~~[˜]~~ ( _nη_ 11 _i/c_ ) 11) [, that]
is: the standard normal density normalized by the total probability
below the truncation point. Draws of _η_ 2 _, η_ 3 _,_ and so on are also taken
from truncated densities, but with different truncation points. Each
of these truncated densities takes the form _[φ]_ [(] _[η][j]_ [)]

Φ( _·_ ) [for some truncation]
point in the denominator. The density from which we draw for the
GHK simulator is therefore:



_φ_ ( _η_ 1) _φ_ ( _η_ 2)
Φ( _−V_ ~~[˜]~~ _n_ 1 _i/c_ 11) _[×]_ Φ( _−_ ( _V_ ~~[˜]~~ _n_ 2 _i_ + _c_ 21 _η_ 1) _/c_ 22) _[×]_ [ etc. for] _[ η][ ∈]_ _[B]_

(5.8)
0 for _η /∈_ _B_



_f_ ( _η_ ) =











Note that we only take draws that are consistent with the person choosing alternative _i_ (since we draw from the correctly truncated distributions). So _f_ ( _η_ ) = 0 for _η /∈_ _B_ .
Recall that for a draw of _η_ within the GHK simulator, we calculate:







_P_ ˇ _in_ ( _η_ ) = Φ


_×_ Φ




_−V_ [˜] _n_ 1 _i_



_c_ 11


_−_ ( _V_ [˜] _n_ 2 _i_ + _c_ 21 _η_ 1)

_c_ 22







_×_ etc. (5.9)


Note that this expression is the denominator of _f_ ( _η_ ) for _η ∈_ _B_, given
in equation (5.8). Using this fact, we can re-write the density _f_ ( _η_ ) as:



_g_ ( _η_ )
_P_ ~~ˇ~~ _ni_ ( _η_ ) [for] _[ η][ ∈]_ _[B]_


0 for _η /∈_ _B_



_f_ ( _η_ ) =











With this expression for _f_ ( _η_ ), we can prove that the GHK simulator, _P_ [ˇ] _in_ ( _η_ ), is unbiased for _Pni_ ( _η_ ):

            _E_ ( _P_ [ˇ] _in_ ( _η_ )) = _P_ ˇ _in_ ( _η_ ) _f_ ( _η_ ) _dη_


_5.6. SIMULATION OF THE CHOICE PROBABILITIES_ 151




  =

  =



_η∈B_ _P_ ˇ _in_ ( _η_ ) _P_ ˇ _[g]_ _in_ [(] _[η]_ ( _η_ [)]



by (5.6.3)
_P_ ˇ _in_ ( _η_ ) _[dη]_



_g_ ( _η_ ) _dη_
_η∈B_




  = _I_ ( _η ∈_ _B_ ) _g_ ( _η_ ) _dη_



= _Pin._


The interpretation of GHK as an importance sampler is also obtained from this expression:

        _Pin_ = _I_ ( _η ∈_ _B_ ) _g_ ( _η_ ) _dη_




  = _I_ ( _η ∈_ _B_ ) _g_ ( _η_ ) _[f]_ [(] _[η]_ [)]



_f_ ( _η_ ) _[dη]_




  _g_ ( _η_ )
= _I_ ( _η ∈_ _B_ ) by (5.6.3)
_g_ ( _η_ ) _/P_ [ˇ] _in_ ( _η_ ) _[f]_ [(] _[η]_ [)] _[dη]_




  = _I_ ( _η ∈_ _B_ ) _P_ [ˇ] _in_ ( _η_ ) _f_ ( _η_ ) _dη_




        = _P_ ˇ _in_ ( _η_ ) _f_ ( _η_ ) _dη_


where the last equality is because _f_ ( _η_ ) _>_ 0 only when _η ∈_ _B_ . The GHK
procedure takes draws from _f_ ( _η_ ), calculates _P_ [ˇ] _in_ ( _η_ ) for each draw, and
averages the results. Essentially, GHK replaces the 0-1 _I_ ( _η ∈_ _B_ ) with
smooth _P_ [ˇ] _in_ ( _η_ ) and makes the corresponding change in the density from
_g_ ( _η_ ) to _f_ ( _η_ ).


152 _CHAPTER 5. PROBIT_


## **Chapter 6**

# **Mixed Logit**

### **6.1 Choice probabilities**

Mixed logit is a highly flexible model that can approximate any random utility model (McFadden and Train, 2000). It resolves the three
limitations of standard logit by allowing for random taste variation,
unrestricted substitution patterns, and correlation in unobserved factors over time. Unlike probit, it is not restricted to normal distributions. Its derivation is straightforward, and simulation of its choice
probabilities is computationally simple.
Like probit, the mixed logit model has been known for many years
but has only become fully applicable since the advent of simulation.
The first application of mixed logit was apparently the automobile demand models created jointly by Boyd and Mellman (1980) and Cardell
and Dunbar (1980). In these studies, the explanatory variables did not
vary over decision-makers and the observed dependent variable was
market shares rather than individual customer’s choices. As a result,
the computationally intensive integration that is inherent in mixed
logit (as explained below) needed to be performed only once for the
market as a whole, rather than for each decision-maker in a sample.
Early applications on customer-level data, such as Train et al. (1987)
and Ben-Akiva et al. (1993), included only one or two dimensions of integration, which could be calculated by quadrature. Improvements in
computer speed and in our understanding of simulation methods have
allowed the full power of mixed logits to be utilized. Among the studies to evidence this power are those by Bhat (1998 _a_ ) and Brownstone
and Train (1999) on cross-sectional data and Erdem (1996), Revelt


153


154 _CHAPTER 6. MIXED LOGIT_


and Train (1998), and Bhat (2000) on panel data. The description in
the current chapter draws heavily from Train (1999).
Mixed logit models can be derived under a variety of different behavioral specifications, and each derivation provides a particular interpretation. The mixed logit model is _defined_ on the basis of the
functional form for its choice probabilities. Any behavioral specification whose derived choice probabilities take this particular form is
called a mixed logit model.
Mixed logit probabilities are the integral of standard logit probabilities over a density of parameters. Stated more explicitly, a mixed
logit model is any model whose choice probabilities can be expressed
in the form: _Pni_ = _Lni_ ( _β_ ) _f_ ( _β_ ) _dβ_


where _Lni_ ( _β_ ) is the logit probability evaluated at parameters _β_ :


_e_ _[V][ni]_ [(] _[β]_ [)]
_Lni_ ( _β_ ) = ~~�~~ _J_
_j_ =1 _[e][V][nj]_ [(] _[β]_ [)]


and _f_ ( _β_ ) is a density function. _Vni_ ( _β_ ) is a portion of utility, which
depends on parameters _β_ . If utility is linear in _β_, then _Vni_ ( _β_ ) = _β_ _[′]_ _xni_ .
In this case, the mixed logit probability takes its usual form:




   - [�]
_e_ _[β][′][x][ni]_
_Pni_ = ~~�~~
_j_ _[e][β]_ ~~_[′]_~~ _[x][nj]_







_f_ ( _β_ ) _dβ._ (6.1)



The mixed logit probability is a weighted average of the logit formula evaluated at different values of _β_, with the weights given by
density _f_ ( _β_ ). In the statistics literature, the weighted average of several functions is called a mixed function, and the density that provides
the weights is called the mixing distribution. Mixed logit is a mixture
of the logit function evaluated at different _β_ ’s with _f_ ( _β_ ) as the mixing
distribution.
Standard logit is a special case where the mixing distribution _f_ ( _β_ )
is degenerate at fixed parameters _b_ : _f_ ( _β_ ) = 1 for _β_ = _b_ and zero for
_β ̸_ = _b_ . The choice probability (6.1) then becomes the simple logit
formula

_e_ _[b][′][x][ni]_
_Pni_ = ~~�~~ _[.]_
_j_ _[e][b]_ ~~_[′]_~~ _[x][nj]_


The mixing distribution _f_ ( _β_ ) can be discrete, with _β_ taking a finite set of distinct values. Suppose _β_ takes _M_ possible values labeled


_6.1. CHOICE PROBABILITIES_ 155



_b_ 1 _, . . ., bM_ with probability _sm_ that _β_ = _bm._ In this case, the mixed
logit becomes the “latent class model” that has long been popular in
psychology and marketing; examples include Kamakura and Russell
(1989) and Chintagunta, Jain and Vilcassim (1991). The choice probability is:








_e_ _[b]_ _m_ _[′]_ _[x][ni]_

~~�~~
_j_ _[e][b]_ ~~_[′]_~~ _[m][x][nj]_



_Pni_ =




- _M_

_sm_
_m_ =1



_._



This specification is useful if there are _M_ segments in the population,
each of which has its own choice behavior or preferences. The share of
the population in segment _m_ is _sm_, which the researcher can estimate
within the model along with the _b_ ’s for each segment.
In most applications that have actually been called mixed logit
(such as those cited in the introductory paragraphs above), _f_ ( _β_ ) is
specified to be continuous. For example, the density of _β_ can be
specified to be normal with mean _b_ and covariance _W_ . The choice
probability under this density becomes:




   - [�]
_e_ _[β][′][x][ni]_
_Pni_ = ~~�~~
_j_ _[e][β]_ ~~_[′]_~~ _[x][nj]_







_φ_ ( _β | b, W_ ) _dβ_



where _φ_ ( _β | b, W_ ) is the normal density with mean _b_ and covariance _W_ .
The researcher estimates _b_ and _W_ . Lognormal, uniform, triangular,
gamma, or any other distribution can be used. As will be shown in section 6.5, by specifying the explanatory variables and density appropriately, the researcher can represent any utility-maximizing behavior by
a mixed logit model, as well as many forms of non-utility-maximizing
behavior.
Tests for the need for a non-degenerate mixing distribution, as
well as the adequacy of any given distribution, have been developed
by McFadden and Train (2000) and Chesher and Santos-Silva (2002).
Several studies have compared discrete and continuous mixing distributions within the context of mixed logit; see, for example, Wedel and
Kamakura (2000) and Ainslie, Andrews and Currim (2001).
An issue of terminology arises with mixed logit models. There
are two sets of parameters in a mixed logit model. First, we have
the parameters _β_, which enter the logit formula. These parameters
have density _f_ ( _β_ ). The second set are parameters that describe this
density. For example, if _β_ is normally distributed with mean _b_ and
covariance _W_, then _b_ and _W_ are parameters that describe the density


156 _CHAPTER 6. MIXED LOGIT_


_f_ ( _β_ ). Usually (though not always, as noted below), the researcher is
interested in estimating the parameters of _f_ .
Denote the parameters that describe the density of _β_ as _θ_ . The
more appropriate way to denote this density is _f_ ( _β | θ_ ). The mixed
logit choice probabilities do not depend on the values of _β_ . These

            probabilities are _Pni_ = _Lni_ ( _β_ ) _f_ ( _β | θ_ ) _dβ_, which is a function of _θ_ .
The parameters _β_ are integrated out. In this sense, the _β_ ’s are similar
to the _εnj_ ’s, in that both are random terms that are integrated out to
obtain the choice probability.
Under some derivations of the mixed logit model, the values of
_β_ have interpretable meaning as representing the tastes of individual
decision-makers. In these cases, the researcher might want to obtain
information about the _β_ ’s for each sampled decision-maker, as well
as the _θ_ that describes the distribution of _β_ ’s across decision-makers.
In Chapter 11, we describe how the researcher can obtain this information based on estimates of _θ_ and the observed choices of each
decision-maker. In the current chapter, we describe the estimation and
interpretation of _θ_, using classical estimation procedures. In Chapter
12, we describe Bayesian procedures that provide information about _θ_
and each decision-maker’s _β_ simultaneously.

### **6.2 Random coefficients**


The mixed logit probability can be derived from utility-maximizing
behavior in several ways that are formally equivalent but provide different interpretations. The most straightforward derivation, and most
widely used in recent applications, is based on random coefficients.
The decision-maker faces a choice among _J_ alternatives. The utility
of person _n_ from alternative _j_ is specified as


_Unj_ = _βn_ _[′]_ _[x][nj]_ [+] _[ ε][nj]_


where _xnj_ are observed variables that relate to the alternative and
decision-maker, _βn_ is a vector of coefficients of these variables for person _n_ representing that person’s tastes, and _εnj_ is a random term that
is iid extreme value. The coefficients vary over decision-makers in the
population with density _f_ ( _β_ ). This density is a function of parameters
_θ_ that represent, for example, the mean and covariance of the _β_ ’s in
the population. This specification is the same as for standard logit
except that _β_ varies over decision-makers rather than being fixed.


_6.2. RANDOM COEFFICIENTS_ 157


The decision-maker knows the value of his own _βn_ and _εnj_ ’s for
all _j_ and chooses alternative _i_ if and only if _Uni > Unj ∀j ̸_ = _i_ . The
researcher observes the _xnj_ ’s but not _βn_ or the _εnj_ ’s. If the researcher
observed _βn_, then the choice probability would be standard logit, since
the _εnj_ ’s are iid extreme value. That is, the probability _conditional_ on
_βn_ is

_e_ _[β]_ _n_ _[′]_ _[x][ni]_
_Lni_ ( _βn_ ) = ~~�~~

_[.]_
_j_ _[e][β][n]_ ~~_[′]_~~ _[x][nj]_


However, the researcher does not know _βn_ and therefore cannot condition on _β_ . The unconditional choice probability is therefore the integral
of _Lni_ ( _βn_ ) over all possible variables of _βn_ :




   - [�]
_e_ _[β][′][x][ni]_
_Pni_ = ~~�~~
_j_ _[e][β]_ ~~_[′]_~~ _[x][nj]_







_f_ ( _β_ ) _dβ_



which is the mixed logit probability (6.1).
The researcher specifies a distribution for the coefficients and estimates the parameters of that distribution. In most applications,
such as Revelt and Train (1998), Mehndiratta (1996), Ben-Akiva and
Bolduc (1996), _f_ ( _β_ ) has been specified to be normal or lognormal:
_β ∼_ _N_ ( _b, W_ ) or _ln_ ( _β_ ) _∼_ _N_ ( _b, W_ ) with parameters _b_ and _W_ that are
estimated. The lognormal distribution is useful when the coefficient
is known to have the same sign for every decision-maker, such as a
price coefficient that is known to be negative for everyone. Revelt and
Train (2000), Hensher and Greene (2001), and Train (2001) have used
triangular and uniform distributions. With the uniform density, _β_ is
distributed uniformly between _b −_ _s_ and _b_ + _s_, where the mean _b_ and
spread _s_ are estimated. The triangular distribution has positive density that starts at _b −_ _s_, rises linearly to _b_, and then drops linearly to
_b_ + _s_, taking the form of a tent or triangle. The mean _b_ and spread
_s_ is estimated, like with the uniform, but the density is peaked instead of flat. These densities have the advantage of being bounded on
both sides, thereby avoiding the problem that can arise with normals
and lognormals of unreasonably large coefficients for some share of
decision-makers. By constraining _s_ = _b_, the researcher can assure that
the coefficients have the same sign for all decision-makers. Siikamaki
(2001) and Siikamaki and Layton (2001) use the Rayleigh distribution
(Johnson, Kotz and Balakrishnan, 1994), which is on one side of zero
like the lognormal but, as these researchers found, can be easier for


158 _CHAPTER 6. MIXED LOGIT_


estimation than the lognormal. Revelt (1999) used truncated normals.
As these examples indicate, the researcher is free to specify a distribution that satisfies his concepts about behavior in his own application.
Variation in tastes that are related to observed attributes of the
decision-maker are captured through specification of the explanatory
variables and/or the mixing distribution. For example, cost might be
divided by the decision-maker’s income to allow the value or relative
importance of cost to decline as income rises. The random coefficient
of this variable then represents the variation over people with the same
income in the value that they place on cost. The mean valuation of
cost declines with income while the variance around the mean is fixed.
Observed attributes of the decision-maker can also enter _f_ ( _β_ ) so that
higher-order moments of taste variation can also depend on attributes
of the decision-maker. For example, Bhat (1998 _a_ ) and Bhat (2000)
specify _f_ ( _β_ ) to be log-normal with the mean and variance being a
function of decision-maker characteristics.

### **6.3 Error-components**


A mixed logit model can be used without a random-coefficients interpretation, as simply representing error components that create correlations among the utilities for different alternatives. Utility is specified
as
_Unj_ = _α_ _[′]_ _xnj_ + _µ_ _[′]_ _n_ _[z][nj]_ [+] _[ ε][nj]_


where _xnj_ and _znj_ are vectors of observed variables relating to alternative _j_, _α_ is a vector of fixed coefficients, _µ_ is a vector of random terms
with zero mean, and _εnj_ is distributed iid extreme value. The terms
in _znj_ are error components that, along with _εnj_, define the stochastic
portion of utility. That is, the unobserved (random) portion of utility is
_ηnj_ = _µ_ _[′]_ _n_ _[z][nj]_ [+] _[ε][nj]_ [, which can be correlated over alternatives depending]
on the specification of _znj_ . For the standard logit model, _znj_ is identically zero, such that there is no correlation in utility over alternatives.
This lack of correlation gives rise to the IIA property and its restrictive
substitution patterns. With non-zero error components, utility is correlated over alternatives: _Cov_ ( _ηni, ηnj_ ) = _E_ ( _µ_ _[′]_ _n_ _[z][ni]_ [+] _[ε][ni]_ [)(] _[µ][′]_ _n_ _[z][nj]_ [+] _[ε][nj]_ [) =]
_zni_ _[′]_ _[Wz][nj]_ [ where] _[ W]_ [ is the covariance of] _[ µ][n]_ [. Utility is correlated over]
alternatives even when, as in most specifications, the error components
are independent such that _W_ is diagonal.


_6.3. ERROR-COMPONENTS_ 159


Various correlation patterns, and hence substitution patterns, can
be obtained by appropriate choice of variables to enter as error components. For example, an analog to nested logit is obtained by specifying a dummy variable for each nest that equals 1 for each alternative
in the nest and zero for alternatives outside the nest. With _K_ nonoverlapping nests, the error components are _µ_ _[′]_ _n_ _[z][nj]_ [=][ �] _[K]_ _k_ =1 _[µ][nk][d][jk]_ [,]
where _djk_ = 1 if _j_ is in nest _k_ and zero otherwise. It is convenient
in this situation to specify the error components to be independently
normally distributed: _µnk_ iid _N_ (0 _, σk_ ). The random term _µnk_ enters
the utility of each alternative in nest _k_, inducing correlation among
these alternatives. It does not enter any of the alternatives in other
nests, thereby not inducing correlation between alternatives in the nest
with those outside the nest. The variance _σk_ captures the magnitude
of the correlation. It plays an analogous role as the “inclusive value
coefficient” of nested logit models.

To be more precise, the covariance between two alternatives in nest
_k_ is _Cov_ ( _ηni, ηnj_ ) = _E_ ( _µk_ + _εni_ )( _µk_ + _εnj_ ) = _σk_ . The variance for each
of the alternatives in nest _k_ is _V ar_ ( _ηni_ ) = _E_ ( _µk_ + _εni_ ) [2] = _σk_ + _π_ [2] _/_ 6,
since the variance of the extreme value term, _εni_, is _π_ [2] _/_ 6 (see section
3.1). The correlation between any two alternatives within nest _k_ is
therefore _σk/_ ( _σk_ + _π_ [2] _/_ 6). Constraining the variance of each nest’s
error component to be the same for all nests (i.e., constraining _σk_ =
_σ, k_ = 1 _, . . ., K_ ), is analogous to constraining the log-sum coefficient
to be the same for all nests in a nested logit. This constraint also
assures that the mixed logit model is normalized for scale and level.

Allowing different variances for the random terms for different nests
is analogous to allowing the inclusive value coefficient to differ across
nests in a nested logit. An analog to overlapping nests is captured
with dummies that identify overlapping sets of alternatives, as in Bhat
(1998 _a_ ). An analog to heteroskedastic logit (discussed in section 4.5)
is obtained by entering an error component for each alternative. BenAkiva, Bolduc and Walker (2001) provide guidance on how to specify
these variables appropriately.

Error-components and random-coefficients specifications are formally equivalent. Under the random-coefficient motivation, utility is
specified as _Unj_ = _βn_ _[′]_ _[x][nj]_ [+] _[ ε][nj]_ [with random] _[ β][n]_ [. The coefficients] _[ β][n]_
can be decomposed into their mean denoted _α_ and deviations denoted
_µn_ such that _Unj_ = _α_ _[′]_ _xnj_ + _µ_ _[′]_ _n_ _[x][nj]_ [+] _[ ε][nj]_ [, which has error components]
defined by _znj_ = _xnj_ . Conversely, under an error-components moti

160 _CHAPTER 6. MIXED LOGIT_


vation, utility is _Unj_ = _α_ _[′]_ _xnj_ + _µ_ _[′]_ _n_ _[z][nj]_ [+] _[ ε][nj]_ [, which is equivalent to]
a random parameters model with fixed coefficients for variables _xnj_
and random coefficients with zero means for variables _znj_ . If _xnj_ and
_znj_ overlap (in the sense that some of the same variables enter _xnj_
and _znj_,) the coefficients of these variables can be considered to vary
randomly with mean _α_ and the same distribution as _µn_ around their
mean.
Though formally equivalent, the way a researcher thinks about the
model affects the specification of the mixed logit. For example, when
thinking in terms of random parameters, it is natural to allow each
variable’s coefficient to vary and perhaps even to allow correlations
among the coefficients. This is the approach pursued by Revelt and
Train (1998). However, when the primary goal is to represent substitution patterns appropriately through the use of error components,
the emphasis is placed on specifying variables that can induce correlations over alternatives in a parsimonious fashion so as to provide
sufficiently realistic substitution patterns. This is the approach taken
by Brownstone and Train (1999). The goals differed in these studies, with Revelt and Train being interested in the pattern of tastes,
while Brownstone and Train were more concerned with prediction. The
number of explanatory variables also differed, with Revelt and Train
examining six variables, such that estimating the joint distribution of
their coefficients was a reasonable goal, while Brownstone and Train
included 26 variables. Expecting to estimate the distribution of 26
coefficients might be unreasonable, and yet thinking in terms of random parameters instead of error components can lead the researcher
to such unreasonable expectations. It is important to remember that
the mixing distribution, whether motivated by random parameters or
error components, captures variance and correlations in unobserved
factors. There is a natural limit on how much one can learn about
things that are not seen.

### **6.4 Substitution patterns**


Mixed logit does not exhibit independence from irrelevant alternatives
(IIA) or the restrictive substitution patterns of logit. The ratio of
mixed logit probabilities _Pni/Pnj_ depends on all the data, including
attributes of alternatives other than _i_ or _j_ . The denominators of the
logit formula are inside the integral and therefore do not cancel. The


_6.5. APPROXIMATION TO ANY RANDOM UTILITY MODEL_ 161



percent change in the probability for one alternative given a change in
the _m_ -th attribute of another alternative is:



_Enix_ _[m]_ _nj_ = _−_ [1]



_Pni_




_β_ _[m]_ _Lni_ ( _β_ ) _Lnj_ ( _β_ ) _f_ ( _β_ ) _dβ_




   -   = _−_ _β_ _[m]_ _Lnj_ ( _β_ ) _Lni_ ( _β_ )




_f_ ( _β_ ) _dβ,_



_Pni_



where _β_ _[m]_ is the _m_ -th element of _β_ . This elasticity is different for each
alternative _i_ . A 10 percent reduction for one alternative need not imply
(as with logit) a 10 percent reduction in each other alternative. Rather,
the substitution pattern depends on the specification of the variables
and mixing distribution, which can be determined empirically.
Note that the percent change in probability depends on the correlation between _Lni_ ( _β_ ) and _Lnj_ ( _β_ ) over different values of _β_, which
is determined by the researcher’s specification of variables and mixing
distribution. For example, to represent a situation where an improvement in alternative _j_ draws more proportionately from alternative _i_
than alternative _k_, the researcher can specify an element of _x_ that is
positively correlated between _i_ and _j_ but uncorrelated or negatively
correlated between _k_ and _j_, with a mixing distribution that allows the
coefficient of this variable to vary.

### **6.5 Approximation to any random utility model**


McFadden and Train (2000) show that any random utility model (RUM)
can be approximated to any degree of accuracy by a mixed logit with
appropriate choice of variables and mixing distribution. This proof is
analogous to the RUM-consistent approximations provided by Dagsvik
(1994). An intuitive explanation can easily be provided. Suppose the
true model is _Unj_ = _αn_ _[′]_ _[z][nj]_ [where] _[ z][nj]_ [are variables related to alter-]
native _j_ and _α_ follows any distribution _f_ ( _α_ ). Any random utility
model can be expressed in this form. (The more traditional notation of _Unj_ = _βn_ _[′]_ _[x][nj]_ [+] _[ ε][nj]_ [is obtained by letting] _[ z]_ _nj_ _[′]_ [=] _[ ⟨][x]_ _nj_ _[′]_ _[, d][j][⟩]_ [and]
_α_ _[′]_ = _⟨βn_ _[′]_ _[, ε][nj][⟩]_ [and] _[ f]_ [(] _[α]_ [) the joint density of] _[ β][n]_ [and] _[ ε][nj]_ _[∀]_ _[j]_ [.) Condi-]
tional on _α_, the person’s choice is fully determined since _Unj_ is then
known for each _j_ . The conditional probability is therefore:

_qni_ ( _α_ ) = _I_ ( _αn_ _[′]_ _[z][ni]_ _[> α]_ _n_ _[′]_ _[z][nj]_ _[∀]_ _[j][ ̸]_ [=] _[ i]_ [)]


where _I_ ( _·_ ) is the 1-0 indicator of whether the event in parentheses
occurs. This conditional probability is deterministic in the sense that


162 _CHAPTER 6. MIXED LOGIT_


the probability is either zero or one: conditional on all the unknown
random terms, the decision-maker’s choice is completely determined.
The unconditional choice probability is the integral of _qni_ ( _α_ ) over _α_ :

         _Qni_ = _I_ ( _αn_ _[′]_ _[z][ni]_ _[> α]_ _n_ _[′]_ _[z][ni]_ _[∀]_ _[j][ ̸]_ [=] _[ i]_ [)] _[f]_ [(] _[α]_ [)] _[dα.]_


We can approximate this probability with a mixed logit. Scale
utility by _λ_, such that _Unj_ _[∗]_ [= (] _[α/λ]_ [)] _[z][nj]_ [. This scaling does not change]
the model since behavior is unaffected by the scale of utility. Then add
an iid extreme value term: _εnj_ . The addition of the extreme value term
_does_ change the model, since it changes the utility of each alternative.
We add it because doing so gives us a mixed logit. And, as we will
show (this is the purpose of the proof), adding the extreme value term
is innocuous. The mixed logit probability based on this utility is:




   - [�]
_e_ [(] _[α/λ]_ [)] _[′][z][ni]_
_Pni_ = ~~�~~
_j_ _[e]_ [(] _[α/λ]_ [)] _[′][z][nj]_







_f_ ( _α_ ) _dβ._



As _λ_ approaches zero, the coefficients _α/λ_ in the logit formula grow
large and _Pni_ approaches a 1-0 indicator for the alternative with the
highest utility. That is, the mixed logit probability _Pni_ approaches the
true probability _Qni_ as _λ_ approaches zero. By scaling the coefficients
upwards sufficiently, the mixed logit based on these scaled coefficients
is arbitrarily close to the true model. Srinivasan and Mahmassani
(2000) use this concept of raising the scale of coefficients to show that
a mixed logit can approximate a probit model; the concept applies
generally to approximate any random utility model.
Recall that we added an iid extreme value term to the true utility of
each alternative. These terms change the model because the alternative
with highest utility before the terms are added might not have highest
utility after adding them (since a different amount is added to each
utility). However, by raising the scale of utility sufficiently, we can be
essentially sure that the addition of the extreme value terms has no
effect. Consider a two alternative example. Suppose, using the true
model with its original scaling, that the utility of alternative 1 is 0 _._ 5
units higher than the utility of alternative 2, such that alternative 1
is chosen. Suppose we add an extreme value term to each alternative.
There’s a good chance, given the variance of these random terms, that
the value obtained for alternative 2 will exceed that for alternative 1 by
at least half a unit, such that alternative 2 obtains the highest utility


_6.6. SIMULATION_ 163


instead of 1 after adding them. The addition of the extreme value terms
changes the model since it changes which alternative has the highest
utility. Suppose, however, that we scale up the original utility by a
factor of 10 (i.e., _λ_ = 0 _._ 10). The utility for alternative 1 now exceeds
the utility for alternative 2 by 5 units. It is highly unlikely that adding
extreme value terms to these utilities will reverse this difference. That
is, it is highly unlikely, in fact next to impossible, that the value of
_εn_ 2 that is added to the utility of alternative 2 is larger by 5 than the
_εn_ 1 that is added to the utility of alternative 1. If scaling up by 10
is not sufficient to assure that adding the extreme value term has no
effect, then the original utilities can be scaled up by 100 or 1000. At
some point, a scale will be found for which the addition of the extreme
value terms has no effect. Stated succinctly: adding an extreme value
term to true utility, which makes the model into a mixed logit, does
not change utility in any meaningful way when the scale of the utility
is sufficiently large. A mixed logit can approximate any random utility
model simply by scaling up utility sufficiently.
This demonstration is not intended to suggest that raising the scale
of utility is actually how the researcher would proceed in specifying a
mixed logit as an approximation to the true model. Rather, the demonstration simply indicates that if no other means for specifying a mixed
logit to approximate the true model can be found, then this re-scaling
procedure can be used to attain the approximation. Usually, a mixed
logit can be specified that adequately reflects the true model without
needing to resort to an upward scaling of utility. For example, the true
model will usually contain some iid term that is added to the utility of
each alternative. Assuming an extreme value distribution for this term
is perhaps close enough to reality to be empirically indistinguishable
from other distributional assumptions for the iid term. In this case,
the scale of utility is determined naturally by the variance of this iid
term. The researcher’s task is simply to find variables and a mixing
distribution that capture the other parts of utility, namely, the parts
that are correlated over alternatives or heteroskedastic.

### **6.6 Simulation**


Mixed logit is well suited to simulation methods for estimation. Utility
is _Unj_ = _βn_ _[′]_ _[x][nj]_ [+] _[ ε][nj]_ [where the the coefficients] _[ β][n]_ [are distributed with]
density _f_ ( _β | θ_ ) where _θ_ refers collectively to the parameters of this


164 _CHAPTER 6. MIXED LOGIT_


distribution (such as the mean and covariance of _β_ ). The researcher
specifies the functional form _f_ ( _·_ ) and wants to estimate the parameters
_θ_ . The choice probabilities are

            _Pni_ = _Lni_ ( _β_ ) _f_ ( _β | θ_ ) _dβ_



where:



_e_ _[β][′][x][ni]_
_Lni_ ( _β_ ) = ~~�~~ _J_ _[.]_
_j_ =1 _[e][β][′][x][nj]_



The probabilities are approximated through simulation for any given
value of _θ_ . (1) Draw a value of _β_ from _f_ ( _β | θ_ ) and label it _β_ _[r]_ with the
superscript _r_ = 1 referring to the first draw. (2) Calculate the logit
formula _Lni_ ( _β_ _[r]_ ) with this draw. (3) Repeat steps 1 and 2 many times,
and average the results. This average is the simulated probability:



_P_ ˇ _ni_ = [1]

_R_




- _R_

_Lni_ ( _β_ _[r]_ )
_r_ =1



where _R_ is the number of draws. _P_ [ˇ] _ni_ is an unbiased estimator of _Pni_
by construction. Its variance decreases as _R_ increases. It is strictly
positive, such that _ln_ ( _P_ [ˇ] _ni_ ) is defined, which is useful for approximating
the log-likelihood function below. _P_ [ˇ] _ni_ is smooth (twice differentiable)
in the parameters _θ_ and the variables _x_, which facilitates the numerical
search for the maximum of the likelihood function and the calculation
of elasticities. And _P_ [ˇ] _ni_ sums to one over alternatives, which is useful
in forecasting.
The simulated probabilities are inserted into the log-likelihood function to give a simulated log-likelihood:




- _J_



_SLL_ =




- _N_


_n_ =1




- _J_

_dnjlnP_ [ˇ] _nj_
_j_ =1



where _dnj_ = 1 if _n_ chose _j_ and zero otherwise. The maximum simulated
likelihood estimator (MSLE), is the value of _θ_ that maximizes _SLL_ .
The properties of this estimator are discussed in Chapter 10. Usually,
different draws are taken for each observation. This procedure maintains independence over decision-makers of the simulated probabilities
that enter _SLL_ . Lee (1992) describes the properties of MSLE when
the same draws are used for all observations.


_6.7. PANEL DATA_ 165


The simulated mixed logit probability can be related to acceptreject (A-R) methods of simulation. A-R simulation is described in
section (5.6) for probit models, but it is applicable more generally.
For any random utility model, the A-R simulator is constructed as
follows: (1) A draw of the random terms is taken. (2) The utility of
each alternative is calculated based on this draw, and the alternative
with the highest utility is identified. (3) Steps 1 and 2 are repeated
many times. (4) The simulated probability for an alternative is calculated as the proportion of draws for which that alternative has the
highest utility. The A-R simulator is unbiased by construction. However, it is not strictly positive for any finite number of draws. It is
also not smooth but rather a step-function: constant within ranges of
parameter for which the identity of the alternative with the highest
utility does not change for any draws, and with jumps where changes
in the parameters change the identity of the alternative with the highest utility. Numerical methods for maximization based on the A-R
simulator are hampered by these characteristics. To address these numerical problems, the A-R simulator can be smoothed by replacing the
0-1 indicator with the logit formula. As discussed in section (5.6.2),
the logit-smoothed A-R simulator can approximate the A-R simulator
arbitrarily closely by scaling utility appropriately.
The mixed logit simulator can be seen as a logit-smoothed A-R
simulator of any random utility model: draws of the random terms
are taken, utility is calculated for these draws, the calculated utilities
are inserted into the logit formula, and the results are averaged. The
theorem that a mixed logit can approximate any random utility model
(section 6.5) can be viewed from this perspective. We know from section (5.6.2) that the logit-smoothed A-R simulator can be arbitrarily
close to the A-R simulator for any model, with sufficient scaling of utility. Since the mixed logit simulator is equivalent to a logit-smoothed
A-R simulator, the simulated mixed logit model can be arbitrarily close
to the A-R simulator of any model.

### **6.7 Panel data**


labelsec:mxpanel
The specification is easily generalized to allow for repeated choices
by each sampled decision-maker. The simplest specification treats the
coefficients that enter utility as varying over people but being constant


