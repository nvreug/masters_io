116 _CHAPTER 5. PROBIT_


zero mean and a covariance matrix that can be expressed explicitly as:



_σ_ 11 _σ_ 12 _σ_ 13 _σ_ 14

_·_ _σ_ 22 _σ_ 23 _σ_ 24

_·_ _·_ _σ_ 33 _σ_ 34

_·_ _·_ _·_ _σ_ 44








 (5.5)




Ω=













where the dots refer to the corresponding elements on the upper part
of the matrix. Note that there are 10 elements in this matrix, that is,
10 distinct _σ_ ’s representing the variances and covariances among the 4
errors. In general, a model with _J_ alternatives has _J_ ( _J_ + 1) _/_ 2 distinct
elements in the covariance matrix of the errors.
To account for the fact that the level of utility is irrelevant, we
take utility differences. In my procedure, I always take differences
with respect to the first alternative, since that simplifies the analysis
in a way that we will see. Define error differences as ˜ _εnj_ 1 = _εnj −_ _εn_ 1
for _j_ = 2 _,_ 3 _,_ 4, and define the vector of error differences as ˜ _εn_ 1 =
_⟨ε_ ˜ _n_ 21 _,_ ˜ _εn_ 31 _,_ ˜ _εn_ 41 _⟩_ . Note that the subscript 1 in ˜ _εn_ 1 means that the error
differences are against the first alternative, rather than that the errors
are for the first alternative. The covariance matrix for the vector of
error differences takes the form











˜Ω1 =





_θ_ 22 _θ_ 23 _θ_ 24

 _·_ _θ_ 33 _θ_ 34

_·_ _·_ _θ_ 44



where the _θ_ ’s relate to the original _σ_ ’s as follows:


_θ_ 22 = _σ_ 22 + _σ_ 11 _−_ 2 _σ_ 12
_θ_ 33 = _σ_ 33 + _σ_ 11 _−_ 2 _σ_ 13
_θ_ 44 = _σ_ 44 + _σ_ 11 _−_ 2 _σ_ 14
_θ_ 23 = _σ_ 23 + _σ_ 11 _−_ _σ_ 12 _−_ _σ_ 13
_θ_ 24 = _σ_ 24 + _σ_ 11 _−_ _σ_ 12 _−_ _σ_ 14
_θ_ 34 = _σ_ 34 + _σ_ 11 _−_ _σ_ 13 _−_ _σ_ 14 _._


Computationally, this matrix can be obtained using the transformation
matrix _Mi_ defined in section (5.1), as Ω [˜] 1 = _M_ 1Ω _M_ 1 _[′]_ [.]
To set the scale of utility, one of the diagonal elements is normalized. I set the top-left element of Ω [˜] 1, which is the variance of ˜ _εn_ 21, to 1.


_5.2. IDENTIFICATION_ 117


This normalization for scale gives us the following covariance matrix:







 (5.6)



˜Ω _[∗]_ 1 [=]





1 _θ_ 23 _[∗]_ _θ_ 24 _[∗]_

 _·_ _θ_ 33 _[∗]_ _θ_ 34 _[∗]_

_·_ _·_ _θ_ 44 _[∗]_ _[.]_



The _θ_ _[∗]_ ’s relate to the original _σ_ ’s as follows:


_σ_ 33 + _σ_ 11 _−_ 2 _σ_ 13
_θ_ 33 _[∗]_ =
_σ_ 22 + _σ_ 11 _−_ 2 _σ_ 12



_σ_ 44 + _σ_ 11 _−_ 2 _σ_ 14
_θ_ 44 _[∗]_ =
_σ_ 22 + _σ_ 11 _−_ 2 _σ_ 12



_σ_ 23 + _σ_ 11 _−_ _σ_ 12 _−_ _σ_ 13
_θ_ 23 _[∗]_ =

_σ_ 22 + _σ_ 11 _−_ 2 _σ_ 12

_σ_ 24 + _σ_ 11 _−_ _σ_ 12 _−_ _σ_ 14
_θ_ 24 _[∗]_ =

_σ_ 22 + _σ_ 11 _−_ 2 _σ_ 12

_σ_ 34 + _σ_ 11 _−_ _σ_ 13 _−_ _σ_ 14
_θ_ 34 _[∗]_ =



_σ_ 22 + _σ_ 11 _−_ 2 _σ_ 12



_σ_ 22 + _σ_ 11 _−_ 2 _σ_ 12



_._
_σ_ 22 + _σ_ 11 _−_ 2 _σ_ 12



There are 5 elements in Ω [˜] _[∗]_ 1 [. These are the only identified parame-]
ters in the model. This number is less than the 10 elements that enter
Ω. Each _θ_ _[∗]_ is a function of the _σ_ ’s. Since there are 5 _θ_ _[∗]_ ’s and 10 _σ_ ’s,
it is not possible to solve for all the _σ_ ’s from estimated values of the
_θ_ _[∗]_ ’s. It is therefore not possible to obtain estimates of all the _σ_ ’s.
In general, a model with _J_ alternatives and an unrestricted covariance matrix will have [( _J −_ 1) _J/_ 2] _−_ 1 covariance parameters when normalized, compared to the _J_ ( _J_ + 1) _/_ 2 parameters when un-normalized.
Only [( _J −_ 1) _J/_ 2] _−_ 1 parameters are identified. This reduction in the
number of parameters is _not_ a restriction. The reduction in the number of parameters is a normalization that simply eliminates irrelevant
aspects of the original covariance matrix, namely the scale and level
of utility. The 10 elements in Ωallow for variance and covariance that
is due simply to scale and level, which has no relevance for behavior.
Only the 5 elements in Ω [˜] _[∗]_ 1 [contain information about the variance and]
covariance of errors independent of scale and level. In this sense, only
the 5 parameters have economic content, and only the 5 parameters
can be estimated.
Suppose now that the researcher places structure on the covariance
matrix. That is, instead of allowing a full covariance matrix for the
errors, the researcher believes that the errors follow a pattern that
implies particular values for, or relations among, the elements in the


118 _CHAPTER 5. PROBIT_


covariance matrix. The researcher restricts the covariance matrix to
incorporate this pattern. Imposing these restrictions is called “placing
structure on the covariance matrix.”

The structure can take various forms, depending on the application.
Yai, Iwakura and Morichi (1997) estimate a probit model of route
choice where the covariance between any two routes depends only on
the length of shared route segments; this structure reduces the number
of covariance parameters to only one, which captures the relation of
the covariance to shared length. Bolduc, Fortin and Fournier (1996)
estimate a model of physicians’ choice of location where the covariance
among locations is a function of their proximity to one another, using
what Bolduc (1992) has called a “generalized autoregressive” structure.
Haaijer _et al._ (1998) place a factor-analytic structure that arises from
random coefficients of explanatory variables; this type of structure is
described in detail in section 5.3 below. Elrod and Keane (1995) place
a factor-analytic structure, but one that arises from error components
rather than random coefficients _per se_ .

Often the structure that is placed will be sufficient to normalize
the model. That is, the restrictions that the researcher imposes on
the covariance matrix to fit her beliefs about the way the errors relate
to each other will also serve to normalize the model. However, this
is not always the case. The examples cited by Bunch and Kitamura
(1989) are cases where the restrictions that the researcher placed on
the covariance matrix seemed sufficient to normalize the model but
actually were not.

The procedure that I give above can be used to determine whether
the restrictions that a researcher places on the covariance matrix are
sufficient to normalize the model. The researcher specifies Ωwith
her restrictions on its elements. Then the procedure above is used
to derive Ω [˜] _[∗]_ 1 [, which is normalized for scale and level. We know that]
each element of Ω [˜] _[∗]_ 1 [is identified. If each of the restricted elements of]
Ωcan be calculated from the elements of Ω [˜] _[∗]_ 1 [, then the restrictions are]
sufficient to normalize the model. In this case, each parameter in the
restricted Ωis identified. On the other hand, if the elements of Ω
cannot be calculated from the elements of Ω [˜] _[∗]_ 1 [, then the restrictions are]
not sufficient to normalize the model and the parameters in Ωare not
identified.

To illustrate this approach, suppose the researcher is estimating a
four-alternative model and assumes that the covariance matrix for the


_5.2. IDENTIFICATION_ 119


errors has the following form:



1 + _ρ_ _ρ_ 0 0

_·_ 1 + _ρ_ 0 0

_·_ _·_ 1 + _ρ_ _ρ_

_·_ _·_ _·_ 1 + _ρ_









 _[.]_



Ω=













This covariance matrix allows the first and second errors to be correlated, the same as the third and fourth alternatives, but allows no
other correlation. The correlation between the appropriate pairs is
_ρ/_ (1 + _ρ_ ). Note that by specifying the diagonal elements as 1 + _ρ_,
the researcher assures that the correlation is between -1 and 1 for any
value of _ρ_, as required for a correlation. Is this model, as specified,
normalized for scale and level? To answer the question, we apply the
procedure described above. First, we take differences with respect to
the first alternative. The covariance matrix of error differences is:











˜Ω1 =





_θ_ 22 _θ_ 23 _θ_ 24

 _·_ _θ_ 33 _θ_ 34

_·_ _·_ _θ_ 44



where the _θ_ ’s relate to the original _σ_ ’s as follows:


_θ_ 22 = 2


_θ_ 33 = 2 + 2 _ρ_


_θ_ 44 = 2 + 2 _ρ_


_θ_ 23 = 1


_θ_ 24 = 1


_θ_ 34 = 1 + 2 _ρ._


We then normalize for scale by setting the top-left element to 1. The
normalized covariance matrix is











˜Ω _[∗]_ 1 [=]





1 _θ_ 23 _[∗]_ _θ_ 24 _[∗]_

 _·_ _θ_ 33 _[∗]_ _θ_ 34 _[∗]_

_·_ _·_ _θ_ 44 _[∗]_



where the _θ_ _[∗]_ ’s relate to the original _σ_ ’s as follows:


_θ_ 33 _[∗]_ = 1 + _ρ_

_θ_ 44 _[∗]_ = 1 + _ρ_


120 _CHAPTER 5. PROBIT_


_θ_ 23 _[∗]_ = 1 _/_ 2

_θ_ 24 _[∗]_ = 1 _/_ 2

_θ_ 34 _[∗]_ = 1 _/_ 2 + _ρ._

Note that _θ_ 33 _[∗]_ [=] _[ θ]_ 44 _[∗]_ [=] _[ θ]_ 34 _[∗]_ _[−]_ [1] _[/]_ [2 and that the other] _[ θ][∗]_ [’s have fixed]
values. There is one parameter in Ω [˜] _[∗]_ 1 [, as there is in Ω. Define] _[ θ]_ [=1+] _[ρ]_ [.]
Then Ω [˜] _[∗]_ 1 [is]  







˜Ω _[∗]_ 1 [=]



1 1 1
 2 2
 _·_ _θ_ _θ −_ [1]



2

_·_ _·_ _θ_







 _._



The original _ρ_ can be calculated directly from _θ_ . For example, if _θ_
is estimated to be 2 _._ 4, then the estimate of _ρ_ is _θ −_ 1 = 1 _._ 4 and the
correlation is 1 _._ 4 _/_ 2 _._ 4 = _._ 58. The fact that the parameters that enter
Ωcan be calculated from the parameters that enter the normalized
covariance matrix Ω [˜] _[∗]_ 1 [means that the original model is normalized for]
scale and level. That is, the restrictions that the researcher placed on
Ωalso provided the needed normalization.
Sometimes restrictions on the original covariance matrix can appear to be sufficient to normalize the model when in fact they do not.
Applying our procedure will determine whether this is the case. Consider the same model as above, but now suppose that the researcher
allows a different correlation between the first and second errors than
between the third and fourth errors. The covariance matrix of errors
is specified to be:



1 + _ρ_ 1 _ρ_ 1 0 0

_·_ 1 + _ρ_ 1 0 0

_·_ _·_ 1 + _ρ_ 2 _ρ_ 2

_·_ _·_ _·_ 1 + _ρ_ 2









 _[.]_



Ω=













The correlation between the first and second errors is _ρ_ 1 _/_ (1 + _ρ_ 1) and
the correlation between the third and fourth errors is _ρ_ 2 _/_ (1 + _ρ_ 2). We
can derive Ω [˜] 1 for error differences and then derive Ω [˜] _[∗]_ 1 [by setting the]
top-left element of Ω [˜] 1 to 1. The resulting matrix is:







˜Ω _[∗]_ 1 [=]



1 1 1
 2 2
 _·_ _θ_ _θ −_ [1]



2

_·_ _·_ _θ_











where now _θ_ = 1+( _ρ_ 1+ _ρ_ 2) _/_ 2. The values of _ρ_ 1 and _ρ_ 2 cannot be calculated from a value of _θ_ . The original model is therefore not normalized


_5.3. TASTE VARIATION_ 121


for scale and level, and the parameters _ρ_ 1 and _ρ_ 2 are not identified.
This fact is somewhat surprising, since only two parameters enter the
original covariance matrix Ω. It would seem, unless the researcher explicitly tested in the manner we have just done, that restricting the
covariance matrix to consist of only two elements would be sufficient
to normalize the model. In this case, however, it is not.
In the normalized model, only the average of the _ρ_ ’s appears:
( _ρ_ 1 + _ρ_ 2) _/_ 2. It is possible to calculate the average _ρ_ from _θ_, simply as _θ −_ 1. This means that the average _ρ_ is identified, but not
the individual values. When _ρ_ 1 = _ρ_ 2, as in the previous example, the
model is normalized because each _ρ_ is equal to the average _ρ_ . However, as we now see, any model with the same average _ρ_ ’s is equivalent,
after normalizing for scale and level. Hence, assuming that _ρ_ 1 = _ρ_ 2 is
no different than assuming that _ρ_ 1 = 3 _ρ_ 2, or any other relation. All
that matters for behavior is the average of these parameters, not their
values relative to each other. This fact is fairly surprising and would
be hard to realize without using our procedure for normalization.
Now that we know how to assure that a probit model is normalized
for level and scale, and hence contains only economically meaningful
information, we can examine how the probit model is used to represent
various types of choice situations. We look at the three issues for which
logit models are limited and show how the limitation is overcome with
probit. These issues are: taste variation, substitution patterns, and
repeated choices over time.

# **5.3 Taste variation**


Probit is particularly well-suited for incorporating random coefficients,
provided that the coefficients are normally distributed. Hausman and
Wise (1978) were the first, to my knowledge, to give this derivation.
Haaijer, Wedel, Vriens and Wansbeek (1998) provide a compelling application. Assume that representative utility is linear in parameters
and that the coefficients vary randomly over decision-makers instead
of being fixed as we have assumed so far in this book. Utility is:
_Unj_ = _βn_ _[′]_ _[x][nj]_ [+] _[ ε][nj]_ [where] _[ β][n]_ [is the vector of coefficients for decision-]
maker _n_ representing that person’s tastes. Suppose the _βn_ is normally distributed in the population with mean _b_ and covariance _W_ :
_βn ∼_ _N_ ( _b, W_ ). The goal of the research is to estimate parameters _b_
and _W_ .


122 _CHAPTER 5. PROBIT_


Utility can be rewritten with _βn_ decomposed into its mean and
deviations from its mean: _Unj_ = _b_ _[′]_ _xnj_ + _β_ [˜] _n_ _[′]_ _[x][nj]_ [+] _[ε][nj]_ [, where ˜] _[β][n]_ [=] _[ b][−][β][n]_ [.]
The last two terms in utility are random; denote their sum as _ηnj_ to
obtain _Unj_ = _b_ _[′]_ _xnj_ + _ηnj_ . The covariance of the _ηnj_ ’s depends on _W_ as
well as the _xnj_ ’s, such that the covariance differs over decision-makers.
The covariance of the _ηnj_ ’s can be described easily for a twoalternative model with one explanatory variable. In this case, utility
is


_Un_ 1 = _βnxn_ 1 + _εn_ 1
_Un_ 2 = _βnxn_ 2 + _εn_ 2 _._


Assume that _βn_ is normally distributed with mean _b_ and variance
_σβ_ . Assume that _εn_ 1 and _εn_ 2 are identically normally distributed with
variance _σε_ . The assumption of independence is for this example and
is not needed in general. Utility is then rewritten as


_Un_ 1 = _bxn_ 1 + _ηn_ 1
_Un_ 2 = _bxn_ 2 + _ηn_ 2 _._


where _ηn_ 1 and _ηn_ 2 are jointly normally distributed. Each has zero
mean: _E_ ( _ηnj_ ) = _E_ ( _β_ [˜] _nxnj_ + _εnj_ ) = 0. The covariance is determined as
follows. The variance of each is _V_ ( _ηnj_ ) = _V_ ( _β_ [˜] _nxnj_ + _εnj_ ) = _x_ [2] _nj_ _[σ][β]_ [ +] _[σ][ε]_ [.]
Their covariance is

_Cov_ ( _ηn_ 1 _, ηn_ 2) = _E_ [( _β_ [˜] _nxn_ 1 + _εn_ 1)( _β_ [˜] _nxn_ 2 + _εn_ 2)]

= _E_ ( _β_ [˜] _n_ [2] _[x][n]_ [1] _[x][n]_ [2] [+] _[ ε][n]_ [1] _[ε][n]_ [2] [+] _[ ε][n]_ [1] _[β]_ [˜] _[b][x][n]_ [2] [+] _[ ε][n]_ [2] _[β]_ [˜] _[n][x][n]_ [1][)]

= _xn_ 1 _xn_ 2 _σβ._



The covariance matrix is








1 0
0 1



Ω =




_x_ [2] _n_ 1 _[σ][β]_ [+] _[ σ][ε]_ _xn_ 1 _xn_ 2 _σβ_
_xn_ 1 _xn_ 2 _σβ_ _x_ [2] _n_ 2 _[σ][β]_ [+] _[ σ][ε]_











= _σβ_




_x_ [2] _n_ 1 _xn_ 1 _xn_ 2
_xn_ 1 _xn_ 2 _x_ [2] _n_ 2



+ _σε_



_._



One last step is required for estimation. Recall that behavior is not
affected by a multiplicative transformation of utility. We therefore
need to set the scale of utility. A convenient normalization for this
case is _σε_ = 1. Under this normalization,












1 0
0 1



_._



Ω= _σβ_




_x_ [2] _n_ 1 _xn_ 1 _xn_ 2
_xn_ 1 _xn_ 2 _x_ [2] _n_ 2



+


_5.4. SUBSTITUTION PATTERNS/NON-IIA_ 123


The values of _xn_ 1 and _xn_ 2 are observed by the researcher, and the
parameters _b_ and _σβ_ are estimated. Thus, the researcher learns both
the mean and variance of the random coefficient in the population.
Generalization to more than one explanatory variable and more than
two alternatives is straightforward.

# **5.4 Substitution patterns/non-IIA**


Probit can represent any substitution pattern. The probit probabilities
do not exhibit the IIA property that gives rise to the proportional
substitution of logit. Different covariance matrices Ωprovide different
substitution patterns, and by estimating the covariance matrix, the
researcher determines the substitution pattern that is most appropriate
for the data.
A full covariance matrix can be estimated, or the researcher can
place structure on the covariance matrix to represent particular sources
of non-independence. This structure usually reduces the number of parameters and facilitates interpretation of the parameters. We consider
first the situation where the researcher estimates a full covariance matrix, and then turn to a situation where the researcher places structure
on the covariance matrix.


**Full covariance: unrestricted substitution patterns**


For notational simplicity, consider a probit model with four alternatives. A full covariance matrix for the unobserved components of utility
takes the form of Ωin (5.5). When normalized for scale and level, the
covariance matrix becomes Ω [˜] _[∗]_ 1 [in (5.6). The elements of ˜Ω] 1 _[∗]_ [are esti-]
mated. The estimated values can represent any substitution pattern;
importantly, the normalization for scale and level does not restrict the
substitution patterns. The normalization only eliminates aspects of Ω
that are irrelevant to behavior.
Note, however, that the estimated values of the _θ_ _[∗]_ ’s provide essentially no interpretable information in themselves (Horowitz, 1991).
For example, suppose _θ_ 33 _[∗]_ [is estimated to be larger than] _[ θ]_ 44 _[∗]_ [. It might]
be tempting to interpret this result as indicating that the variance in
unobserved utility of the third alternative is greater than that for the
fourth alternative; that is, that _σ_ 33 _> σ_ 44. However, this interpretation
is incorrect. It is quite possible that _θ_ 33 _[∗]_ _[> θ]_ 44 _[∗]_ [and yet] _[ σ]_ [44] _[ > σ]_ [33][, if]


124 _CHAPTER 5. PROBIT_


covariance _σ_ 13 is sufficiently greater than _σ_ 14. Similarly, suppose that
_θ_ 23 is estimated to be negative. This does not mean that unobserved
utility for the second alternative is negatively correlated with unobserved utility for the third alternative (that is, _σ_ 23 _<_ 0). It is possible
that _σ_ 23 is positive and yet _σ_ 12 and _σ_ 13 are sufficiently large to make
_θ_ 23 _[∗]_ [negative. The point here is: estimating a full covariance matrix]
allows the model to represent any substitution pattern but renders the
estimated parameters essentially uninterpretable.


**Structured covariance: restricted substitution patterns**


By placing structure on the covariance matrix, the estimated parameters usually become more interpretable. The structure is a restriction
on the covariance matrix and, as such, reduces the ability of the model
to represent various substitution patterns. However, if the structure
is correct (that is, actually represents the behavior of the decisionmakers), then the true substitution pattern will be able to be represented by the restricted covariance matrix.


Structure is necessarily situation-dependent: an appropriate structure for a covariance matrix depends on the specifics of the situation
being modeled. Several studies using different kinds of structure were
described above in section 5.2. As an example of how structure can be
placed on the covariance matrix and hence substitution patterns, consider a homebuyer’s choice among purchase-money mortgages. Suppose four mortgages are available to the homebuyer from four different institutions: one with a fixed rate, and three with variable rates.
Suppose the unobserved portion of utility consists of two parts: the
homebuyer’s concern about the risk of rising interest rates, labeled _rn_,
which is common to all the variable rate loans, and all other unobserved factors, labeled collectively _ηnj_ . The unobserved component of
utility is then


_εnj_ = _−rndj_ + _ηnj_


where _dj_ = 1 for the variable rate loans and zero for the fixed rate loan,
and the negative sign indicates that utility decreases as concern about
risk rises. Assume that _rn_ is normally distributed over homebuyers
with variance _σ_, and that _ηnj ∀_ _j_ is iid normal with zero mean and


_5.4. SUBSTITUTION PATTERNS/NON-IIA_ 125


variance _ω_ . Then the covariance matrix for _εn_ = _⟨εn_ 1 _, . . ., εn_ 4 _⟩_ is



0 0 0 0

_·_ _σ_ _σ_ _σ_

_·_ _·_ _σ_ _σ_

_·_ _·_ _·_ _σ_













1 0 0 0

_·_ 1 0 0

_·_ _·_ 1 0

_·_ _·_ _·_ 1









 [+] _[ ω]_













Ω=













The model needs to normalized for scale but, as we will see, is already
normalized for level. The covariance of error differences is







 + _ω_





2 1 1

 _·_ 2 1

_·_ _·_ 2







 _._



˜Ω1 =





_σ_ _σ_ _σ_

 _·_ _σ_ _σ_

_·_ _·_ _σ_



This matrix has no fewer parameters than Ω. In this sense, the model
was already normalized for level. To normalize for scale, set _σ_ +2 _ω_ = 1.
Then the covariance matrix becomes:











˜Ω _[∗]_ 1 [=]





1 _θ_ _θ_

 _·_ 1 _θ_

_·_ _·_ 1



where _θ_ = ( _σ_ + _ω_ ) _/_ ( _σ_ +2 _ω_ ). The values of _σ_ and _ω_ cannot be calculated
from _θ_ . However, the parameter _θ_ provides information about the
variance in utility due to concern about risk relative to that due to all
other unobserved factors. For example, suppose _θ_ is estimated to be
0.75. This estimate can be intrepreted as indicating that the variance
in utility attributable to concern about risk is twice as large as the
variance in utility attributable to all other factors:


_θ_ = 0 _._ 75
_σ_ + _ω_
= 0 _._ 75
_σ_ + 2 _ω_

_σ_ + _ω_ = 0 _._ 75 _σ_ + 1 _._ 5 _ω_


_._ 25 _σ_ = _._ 5 _ω_


_σ_ = 2 _ω._


Stated equivalently, _θ_ [ˆ] = 0 _._ 75 means that concern about risk accounts
for two-thirds of the variance in the unobserved component of utility.
Since the original model was already normalized for level, the model
could be estimated without reexpressing the covariance matrix in terms
of error differences. The normalization for scale could be accomplished


126 _CHAPTER 5. PROBIT_


simply by setting _ω_ = 1 in the original Ω. Under this procedure, the
parameter _σ_ is estimated directly. Its value relative to 1 indicates
the variance due to concern about risk relative to the variance due to
perceptions about ease of dealing with each institution. An estimate
_θ_ ˆ = 0 _._ 75 corresponds to an estimate ˆ _σ_ = 2.

# **5.5 Panel data**


Probit with repeated choices is similar to probit on one choice per
decision-maker. The only difference is that the dimension of the covariance matrix of the errors is expanded. Consider a decision-maker
who faces a choice among _J_ alternatives in each of _T_ time periods or
choices situations. The alternatives can change over time, and _J_ and
_T_ can differ for different decision-makers; however, we suppress the notation for these possibilities. The utility that decision-maker _n_ obtains
from alternative _j_ in period _t_ is _Unjt_ = _Vnjt_ + _εnjt_ . In general, one
would expect _εnjt_ to be correlated over time as well as over alternatives,
since factors that are not observed by the researcher can persist over
time. Denote the vector of errors for all alternatives in all times periods as _εn_ = _⟨εn_ 11 _, . . ., εnJ_ 1 _, εn_ 12 _, . . ., εnJ_ 2 _, . . ., εn_ 1 _T, . . ., εnJT ⟩_ . The
covariance matrix of this vector is denoted Ω, which has dimension
_JT × JT_ .
Consider a sequence of alternatives, one for each time period, **i** =
_{i_ 1 _, . . ., iT }_ . The probability that the decision-maker makes this sequence of choices is


_Pn_ **i** = _Prob_ ( _Unitt > Unjt ∀_ _j ̸_ = _it, ∀_ _t_ )



= _Prob_ ( _Vnitt_ + _εnitt > Vnjt_ + _εnjt ∀_ _j ̸_ = _it, ∀_ _t_ )




  =



_φ_ ( _εn_ ) _dεn._
_εn∈Bn_



where _Bn_ = _{εn_ s.t. _Vnitt_ + _εnitt > Vnjt_ + _εnjt ∀_ _j ̸_ = _it, ∀_ _t}_ and _φ_ ( _εn_ ) is
the joint normal density with zero mean and covariance Ω. Compared
to the probit probability for one choice situation, the integral is simply
expanded to be over _JT_ dimensions rather than _J_ .
It is often more convenient to work in utility differences. The probability of sequence **i** is the probability that the utility differences are
negative for each alternative in each time period, when the differences
in each time period are taken against the alternative identified by **i** for


_5.5. PANEL DATA_ 127


that time period:



_Pn_ **i** = _Prob_ ( _U_ [˜] _njitt <_ 0 _∀_ _j ̸_ = _it, ∀_ _t_ )




  =



_φ_ (˜ _εn_ ) _dε_ ˜ _n._
_ε_ ˜ _n∈B_ [˜] _n_



where _U_ [˜] _njitt_ = _Unjt−Unitt_ ; ˜ _ε_ _[′]_ _n_ [=] _[ ⟨]_ [(] _[ε][n]_ [11] _[−][ε][ni]_ 1 [1][)] _[, . . .,]_ [ (] _[ε][nJ]_ [1] _[−][ε][ni]_ 1 [1][)] _[, . . .,]_ [ (] _[ε][n]_ [1] _[T]_ _[−]_
_εniT T_ ) _, . . .,_ ( _εnJT −_ _εniT T_ ) _⟩_ with each _. . ._ being over all alternatives except _it_ ; and the matrix _B_ [˜] _n_ is the set of ˜ _εn_ ’s for which _U_ [˜] _njitt <_ 0 _∀_ _j ̸_ =
_it, ∀_ _t_ . This is a ( _J −_ 1) _T_ dimensional integral. The density _φ_ (˜ _εn_ )
is joint normal with covariance matrix derived from Ω. Simulation of
the choice probability is the same as for situations with one choice per
decision-maker, which we describe in section (5.6), but with a larger
dimension for the covariance matrix and integral. Borsch-Supan _et al._
(1991) provide an example of a multinomial probit on panel data that
allows covariance over time and over alternatives.
For binary choices, such as whether a person buys a particular
product in each time period or works at a paid job each month, the
probit model simplifies considerably (Gourieroux and Monfort, 1993).
The net utility of taking the action (e.g., working) in period _t_ is _Unt_ =
_Vnt_ + _εnt_, and the person takes the action if _Unt >_ 0. This utility is
called net utility because it represents the difference between the utility
of taking the action compared to not taking the action. As such, it is
already expressed in difference terms. The errors are correlated over
time, and the covariance matrix for _εn_ 1 _, . . ., εnT_ is Ω, which is _T × T_ .
A sequence of binary choices is most easily represented by a set of
_T_ dummy variables: _dnt_ = 1 if person _n_ took the action in period _t_
and _dnt_ = _−_ 1 otherwise. The probability of the sequence of choices
_dn_ = _dn_ 1 _, . . ., dnT_ is


_Pndn_ = _Prob_ ( _Untdnt >_ 0 _∀_ _t_ )



= _Prob_ ( _Vntdnt_ + _εntdnt >_ 0 _∀_ _t_ )




  =



_φ_ ( _εn_ ) _dεn_
_εn∈Bn_



where _Bn_ is the set of _εn_ ’s for which _Vntdnt_ + _εntdnt >_ 0 _∀_ _t_, and _φ_ ( _εn_ )
is the joint normal density with covariance Ω.
Structure can be placed on the covariance of the errors over time.
Suppose in the binary case, for example, that the error consists of a
portion that is specific to the decision-maker reflecting his proclivity


128 _CHAPTER 5. PROBIT_


to take the action, and a part that varies over time for each decisionmaker: _εnt_ = _ηn_ + _µnt_ where _µnt_ is iid over time and people with
a standard normal density, and _ηn_ is iid over people with a normal
density with zero mean and variance _σ._ The variance of the error in
each period is _V_ ( _εnt_ ) = _V_ ( _ηn_ + _µnt_ ) = _σ_ + 1. The covariance between
the errors in two different periods _t_ and _s_ is _Cov_ ( _εnt, εns_ ) = _E_ ( _ηn_ +
_µnt_ )( _ηn_ + _µns_ ) = _σ_ . The covariance matrix therefore takes the form:



_σ_ + 1 _σ_ _. . ._ _. . ._ _σ_
_σ_ _σ_ + 1 _σ_ _. . ._ _σ_

_·_ _·_ _·_ _·_ _·_
_σ_ _. . ._ _. . ._ _σ_ _σ_ + 1









 _[.]_



Ω=













Only one parameter, _σ_, enters the covariance matrix. Its value indicates the variance in unobserved utility across individuals (the variance
of _ηn_ ) relative to the variance across time for each individual (the variance of _µnt_ ). It is often called “the cross-subject variance relative to
the within-subject variance.”
The choice probabilities under this structure on the errors can be
easily simulated using the concepts of convenient error partitioning
from section 1.2. Conditional on _ηn_, the probability of _not_ taking
the action in period _t_ is _Prob_ ( _Vnt_ + _ηn_ + _µnt <_ 0) = _Prob_ ( _µnt <_

_−_ ( _Vnt_ + _ηn_ )) = Φ( _−_ ( _Vnt_ + _ηn_ )), where Φ( _·_ ) is the cumulative standard
normal function. Most software packages include routines to calculate
this function. The probability of taking the action, conditional on _ηn_, is
then 1of choices _−_ Φ( _d−n_, conditional on( _Vnt_ + _ηn_ )) = Φ( _ηVnnt_, is therefore+ _ηn_ ). The probability of the sequence [�] _t_ [Φ((] _[V][nt]_ [+] _[η][n]_ [)] _[d][nt]_ [), which]
we can label _Hndn_ ( _ηn_ ). So far we have conditioned on _ηn_, when in fact
_ηn_ is random. The _unconditional_ probability is the integral of the
conditional probability _Hndn_ ( _ηn_ ) over all possible values of _ηn_ :

            _Pndn_ = _Hndn_ ( _ηn_ ) _φ_ ( _ηn_ ) _dηn_


where _φ_ ( _ηn_ ) is the normal density with zero mean and variance _σ_ . This
probability can be simulated very simply as follows. (1) Take a draw
of from a standard normal density using a random number generator.
Multiply the draw by _[√]_ ~~_σ_~~ so that it becomes a draw of _ηn_ from a normal
density with variance _σ_ . (2) For this draw of _ηn_, calculate _Hndn_ ( _ηn_ ).
(3) Repeat steps 1-2 many times and average the results. This average
is a simulated approximation to _Pndn_ . This simulator is much easier


_5.5. PANEL DATA_ 129


to calculate than the general probit simulators described in the next
section. The ability to use this simulator arises from the structure
that we placed on the model, namely that the time-dependence of the
unobserved factors is captured entirely by a random component _ηn_ that
remains constant over time for each person. Gourieroux and Monfort
(1993) provide an example of the use of this simulator with a probit
model of this form.


The representative utility in one time period can include exogenous
variables for other time periods, the same as we discussed with respect
to logit models on panel data (section 3.3.3). That is, _Vnt_ can include
exogenous variables that relate to periods other than _t_ . For example,
a lagged response to price changes can be represented by including
prices from previous periods in the current period’s _V_ . Anticipatory
behavior (by which, for example, a person buys a product now because
he correctly anticipates that the price will rise in the future) can be
represented by including prices in future periods in the current period’s
_V_ .


Entering a lagged dependent variable is possible but introduces two
difficulties that the researcher must address. First, since the errors are
correlated over time, the choice in one period is correlated with the errors in subsequent periods. As a result, inclusion of a lagged dependent
variable without adjusting the estimation procedure appropriately results in inconsistent estimates. This issue is analogous to regression
analysis, where the ordinary least squares estimator is inconsistent
when a lagged dependent variable is included and the errors are serially correlated. To estimate a probit consistently in this situation, the
researcher must determine the distribution of each _εnt_ conditional on
the value of the lagged dependent variables. The choice probability is
then based on this conditional distribution instead of the unconditional
distribution _φ_ ( _·_ ) that we use above. Second, often the researcher does
not observe the decision-makers’ choices from the very first choice that
was available to them. For example, a researcher studying employment
patterns will perhaps observe a person’s employment status over a period of time (e.g., from 1998-2001), but usually will not observe the
person’s employment status starting with the very first time the person could have taken a job (which might precede 1998 by many years).
In this case, the probability for the first period that the researcher
observes depends on the choices of the person in the earlier periods
that the researcher does not observe. The researcher must determine


130 _CHAPTER 5. PROBIT_


a way to represent the first choice probability that allows for consistent estimation in the face of missing data on earlier choices. This is
called the “initial conditions problem” of dynamic choice models. Both
of these issues, as well as potential approaches to dealing with them,
are addressed by Heckman (1981 _b_, 1981 _a_ ) and Heckman and Singer
(1986). Due to their complexity, I do not describe the procedures here
and refer interested and brave readers to these articles.
Papatla and Krishnamurthi (1992) avoid these issues in their probit model with lagged dependent variables by assuming that the unobserved factors are independent over time. As we discussed in relation
to logit on panel data (section 3.3.3), lagged dependent variables are
not correlated with the current errors when the errors are independent
over time and can therefore be entered without inducing inconsistency.
Of course, this procedure is only appropriate if the assumption of errors being independent over time is true in reality, rather than just by
assumption.

# **5.6 Simulation of the choice probabilities**


The probit probabilities do not have a closed-form expression and must
be approximated numerically. Several non-simulation procedures have
been used and can be effective in certain circumstances. Quadrature
methods approximate the integral by a weighted function of specially
chosen evaluation points. A good explanation for these procedures is
provided by Geweke (1996). Examples of their use for probit include
Butler and Moffitt (1982) and Guilkey and Murphy (1993). Quadrature operates effectively when the dimension of the integral is small,
but not with higher dimensions. It can be used for probit if the number
of alternatives (or, with panel data, the number of alternatives times
the number of time periods) is no more than 4 or 5. It can also be
used if the researcher has specified an error-component structure with
no more than 4 or 5 terms. However, it is not effective for general
probit models. And even with low-dimensional integration, simulation
is often easier. Another non-simulation procedure that has been suggested is the Clark algorithm, introduced by Daganzo, Bouthelier and
Sheffi (1977). This algorithm utilizes the fact, shown by Clark (1961),
that the maximum of several normally distributed variables is itself approximately normally distributed. Unfortunately, the approximation
can be highly inaccurate in some situations (as shown by Horowitz,


_5.6. SIMULATION OF THE CHOICE PROBABILITIES_ 131


Sparmann and Daganzo (1982)), and the degree of accuracy is difficult
to assess in any given setting.
Simulation has proven to be very general and useful for approximating probit probabilities. Numerous simulators have been proposed
for probit models; a summary is given by Hajivassiliou, McFadden
and Ruud (1996). In the section above, I described a simulator that
is appropriate for a probit model that has a particularly convenient
structure, namely a binary probit on panel data where the time dependence is captured by one random factor. In the current section, I
describe three simulators that are applicable for probits of any form:
accept-reject, smoothed accept-reject, and GHK. The GHK simulator
is by far the most widely used probit simulator, for reasons that we
discuss. The other two methods are valuable pedagogically. They also
have relevance beyond probit and can be applied in practically any
situation. They can be very useful when the researcher is developing
her own models rather than using probit or any other model in this
book.


**5.6.1** **Accept-reject simulator**


Accept-reject (A-R) is the most straightforward of any simulator. Consider simulating _Pni_ . Draws of the random terms are taken from their
distribution. For each draw, the researcher determines whether that
value of the errors, when combined with the observed variables as faced
by person _n_, would result in alternative _i_ being chosen. If so, the draw
is called an “accept.” If the draw would result in some other alternative being chosen, the draw is a “reject”. The simulated probability is
the proportion of draws that are accepts. This procedure can be applied to any choice model with any distribution for the random terms.
It was originally proposed for probits (Manski and Lerman, 1981), and
we give the details of the approach in terms of the probit model. Its
use for other models is obvious.
We use expression (5.1) for the probit probabilities:


        _Pni_ = _I_ ( _Vni_ + _εni > Vnj_ + _εnj ∀_ _j ̸_ = _i_ ) _φ_ ( _εn_ ) _dεn_


where _I_ ( _·_ ) is an indicator of whether the statement in parentheses holds
and _φ_ ( _εn_ ) is the joint normal density with zero mean and covariance
Ω. The accept-reject simulator of this integral is calculated as follows.


132 _CHAPTER 5. PROBIT_


1. Draw a value of the _J_ -dimensional vector of errors, _εn_, from a
normal density with zero mean and covariance Ω. Label the draw
_ε_ _[r]_ _n_ [with] _[ r]_ [ = 1 and the elements of the draw as] _[ ε]_ _n_ _[r]_ 1 _[, . . ., ε][r]_ _nJ_ [.]


2. Using these values of the errors, calculate the utility that each
alternative obtains with these errors. That is, calculate _Unj_ _[r]_ [=]
_Vnj_ + _ε_ _[r]_ _nj_ _[∀]_ _[j]_ [.]


3. Determine whether the utility of alternative _i_ is greater than
that for all other alternatives. That is, calculate _I_ _[r]_ = 1 if _Uni_ _[r]_ _[>]_
_Unj_ _[r]_ [, indicating an “accept”, and] _[ I]_ _[r]_ [ = 0 otherwise, indicating a]
“reject.”


4. Repeat steps 1-3 many times. Label the number of repetitions
(including the first) as R, such that r takes values of 1 through
R.


5. The simulated probability is the proportion of draws that are
accepts: _P_ [ˇ] _ni_ = _R_ [1]   - _Rr_ =1 _[I]_ _[r]_ [.]

       -        The integral _I_ ( _·_ ) _φ_ ( _εn_ ) _dε_ is approximated by the average _R_ 1 _I_ _r_ ( _·_ )
for draws from _φ_ ( _·_ ). Obviously, _P_ [ˇ] _ni_ is unbiased for _Pni_ : _E_ ( _P_ [ˇ] _ni_ ) =

 - _R_ 1 _E_ [ _I_ _r_ ( _·_ )] = _R_ 1 _Pni_ = _Pni_, where the expectation is over different

sets of R draws. The variance of _P_ [ˇ] _ni_ over different sets of draws diminishes as the number of draws rises. The simulator is often called
the “crude frequency simulator,” since it is the frequency of times that
draws of the errors result in the specified alternative being chosen. The
word “crude” distinguishes it from the “smoothed” frequency simulator that we describe in the next section.
The first step of the A-R simulator for a probit model is to take a
draw from a joint normal density. The question arises: how are such
draws obtained? The most straightforward procedure is that described
in section (9.2.5) which uses the Choleski factor. The covariance matrix
for the errors is Ω. A Choleski factor of Ωis a lower-triangular matrix
_L_ such that _LL_ _[′]_ = Ω. It is sometimes called the generalized square root
of Ω. Most statistical software packages contain routines to calculate
the Choleski factor of any symmetric matrix. Now suppose that _η_ is a
vector of _J_ iid standard normal deviates, such that _η ∼_ _N_ (0 _, I_ ) where
I is the identity matrix. This vector can be obtained by taking J draws
from a random number generator for the standard normal and stacking
them into a vector. We can construct a vector _ε_ that is distributed


_5.6. SIMULATION OF THE CHOICE PROBABILITIES_ 133


_N_ ( _O,_ Ω) by using the Choleski factor to tranform _η_ . In particular,
calculate _ε_ = _Lη_ . Since the sum of normals is normal, _ε_ is normally
distributed. Since _η_ has zero mean, so does _ε_ . The covariance of _ε_ is
_Cov_ ( _ε_ ) = _E_ ( _εε_ _[′]_ ) = _E_ ( _Lη_ ( _Lη_ ) _[′]_ ) = _E_ ( _Lηη_ _[′]_ _L_ _[′]_ ) = _LE_ ( _ηη_ _[′]_ ) _L_ _[′]_ = _LIL_ _[′]_ =
_LL_ _[′]_ = Ω.
Using the Choleski factor _L_ of Ω, the first step of the A-R simulator
becomes two substeps:


1A Draw _J_ values from a standard normal density using a random
number generator. Stack these values into a vector and label the
vector _η_ _[r]_ .


1B Calculate _ε_ _[r]_ _n_ [=] _[ Lη][r]_ [.]

Then, using _ε_ _[r]_ _n_ [, calculate the utility of each alternative and see whether]
alternative _i_ has the highest utility.
The procedure that we have described operates on utilities and expression (5.1), which is a _J_ dimensional integral. The procedure can be
applied analogously to utility differences, which reduces the dimension
of the integral to _J −_ 1. As given in (5.3), the choice probabilities can
be expressed in terms of utility differences:

         _Pni_ = _I_ ( _V_ [˜] _nji_ + ˜ _εnji <_ 0 _∀_ _j ̸_ = _i_ ) _φ_ (˜ _εni_ ) _dε_ ˜ _ni_


where _φ_ (˜ _εni_ ) is the joint normal density with zero mean and covariance Ω [˜] _i_ = _Mi_ Ω _Mi_ _[′]_ [. This integral can be simulated with accept-reject]
methods through the following steps.

1. Draw ˜ _ε_ _[r]_ _ni_ [=] _[ L][i][η][r]_ [ as follows:]


(a) Draw _J −_ 1 values from a standard normal density using a
random number generator. Stack these values into a vector
and label the vector _η_ _[r]_ .

(b) Calculate ˜ _ε_ _[r]_ _ni_ [=] _[ L][i][η][r]_ [, where] _[ L][i]_ [ is the Choleski factor of ˜Ω] _[i]_ [.]


2. Using these values of the errors, calculate the utility difference
for each alternative, differenced against the utility of alternative
_i_ . That is, calculate _U_ [˜] _nji_ _[r]_ [=] _[ V][nj][ −]_ _[V][ni]_ [ + ˜] _[ε]_ _nji_ _[r]_ _[∀]_ _[j][ ̸]_ [=] _[ i]_ [.]


3. Determine whether each utility difference is negative. That is,
calculate _I_ _[r]_ = 1 if _Unji_ _[r]_ _[<]_ [ 0] _[ ∀]_ _[j][ ̸]_ [=] _[ i]_ [, indicating an “accept”, and]
_I_ _[r]_ = 0 otherwise, indicating a “reject.”


134 _CHAPTER 5. PROBIT_


4. Repeat steps 1-3 R times.


5. The simulated probability is the number of accepts divided by
the number of repetitions: _P_ [ˇ] _ni_ = _R_ [1]    - _Rr_ =1 _[I]_ _[r]_ [.]


Using utility differences is slightly faster computationally than using the utilities themselves, since one dimension is eliminated. However, it is often easier conceptually to remain with utilities.
As stated above, the A-R simulator is very general. It can be applied to any model for which draws can be obtained for the random
terms and the behavior that the decision-maker would exhibit with
these draws can be determined. It is also very intuitive, which is an
advantage from a programming perspective since debugging becomes
comparatively easy. However, the A-R simulator has several disadvantages, particularly when used in the context of maximum likelihood
estimation.
Recall that the log-likelihood function is _LL_ = [�] _n_   - _j_ _[d][nj][logP][nj]_
where _dnj_ = 1 if _n_ chose _j_ and 0 otherwise. When the probabilities
cannot be calculated exactly, as in the case of probit, the simulated loglikelihood function is used instead, with the true probabilities replaced
with the simulated probabilities: _SLL_ = [�] _n_ - _j_ _[d][nj][log]_ [ ˇ] _[P][nj]_ [. The value]
of the parameters that maximizes _SLL_ is called the maximum simulated likelihood estimator (MSLE). It is by far the most widely used
simulation-based estimation procedure. Its properties are described in
Chapter 8. Unfortunately, using the A-R simulator in _SLL_ can be
problematic.
There are two issues. First, _P_ [ˇ] _ni_ can be zero for any finite number
of draws _R_ . That is, it is possible that each of the _R_ draws of the
error terms result in a “reject,” such that the simulated probability
is zero. Zero values for _P_ [ˇ] _ni_ are problematic because the log of _P_ [ˇ] _ni_ is
taken when it enters the log-likelihood function and the log of zero is
undefined. _SLL_ cannot be calculated if the simulated probability is
zero for any decision-maker in the sample.
The occurrence of a zero simulated probability is particularly likely
when the true probability is low. Often at least one decision-maker in
a sample will have made a choice that has a low probability. With
numerous alternatives (such as thousands of makes and models for the
choice of car) each alternative has a low probability. With repeated
choices, the probability for any sequence of choices can be extremely
small; for example, if the probability of choosing an alternative is 0 _._ 25


_5.6. SIMULATION OF THE CHOICE PROBABILITIES_ 135


in each of 10 time periods, the probability of the sequence is (0 _._ 25) [10],
which is less than 0.000001.
Furthermore, _SLL_ needs to be calculated at each step in the search
for its maximum. Some of the parameters values at which _SLL_ is calculated can be far from the true values. Low probabilities can occur at
these parameter values even when they do not occur at the maximizing
values.
Non-zero simulated probabilities can always be obtained by taking
enough draws. However, if the researcher continues taking draws until at least one “accept” is obtained for each decision-maker, then the
number of draws becomes a function of the probabilities. The simulation process is then not independent of the choice process that is being
modeled, and the properties of the estimator become more complex.
There is a second difficulty with the A-R simulator for MSLE.
The simulated probabilities are not smooth in the parameters; that
is, they are not twice differentiable. As explained in Chapter 8, the
numerical procedures that are used to locate the maximum of the loglikelihood function rely on the first derivatives, and sometimes the
second derivatives, of the choice probabilities. If these derivatives do
not exist, or do not point toward the maximum, then the numerical
procedure will not perform effectively.
The A-R simulated probability is a step function, as depicted in
Figure 5.1. _P_ [ˇ] _ni_ is the proportion of draws for which alternative _i_ has
the highest utility. An infinitesimally small change in a parameter will
usually not change any draw from being a reject to an accept, or vice
versa. If _Uni_ _[r]_ [is below] _[ U]_ _nj_ _[r]_ [for some] _[ j]_ [ at a given level of the parameters,]
then it will also be below for an infinitesimally small change in any
parameter. So, usually, _P_ [ˇ] _nj_ is constant with respect to small changes
in the parameters. Its derivative with respect to the parameters is
zero in this range. If the parameters change in a way that a reject
becomes an accept, then _P_ [ˇ] _nj_ rises by a discrete amount, from _M/R_ to
( _M_ +1) _/R_ where _M_ is the number of accepts at the original parameter
values. _P_ [ˇ] _nj_ is constant (zero slope) until an accept becomes a reject or
vice versa, at which point _P_ [ˇ] _nj_ jumps by 1 _/R_ . Its slope at this point is
undefined. The first derivative of _P_ [ˇ] _nj_ with respect to the parameters
is either zero or undefined.
The fact that the slope is either zero or undefined hinders the numerical procedures that are used to locate the maximum of _SLL_ . As
discussed in Chapter 8, the maximization procedures use the gradient


136 _CHAPTER 5. PROBIT_


_~_
_Pni_


3/ _R_


2/ _R_


1/ _R_


β


Figure 5.1: The A-R simulator is a step function in parameters.


at trial parameter values to determine the direction to move to find parameters with higher _SLL_ . With the slope _P_ [ˇ] _nj_ for each _n_ either zero
or undefined, the gradient of _SLL_ is either zero or undefined. This
gradient provides no help in finding the maximum.
This issue is not actually as drastic as it seems. The gradient of
_SLL_ can be approximated as the change in _SLL_ for a non-infinitesimally
small change in the parameters. The parameters are changed by an
amount that is large enough to switch accepts to rejects and vice versa
for at least some of the observations. The approximate gradient, which
can be called an arc gradient, is calculated as the amount that _SLL_
changes divided by the change in the parameters. To be precise: for
parameter vector _β_ of length _K_, the derivate of _SLL_ with respect to
the _k_ -th parameter is calculated as ( _SLL_ [1] _−_ _SLL_ [0] ) _/_ ( _βk_ [1] _[−]_ _[β]_ _k_ [0][), where]
_SLL_ [0] is calculated at the original _β_ with _k_ -th element _βk_ [0] [and] _[ SLL]_ [1]

is calculated at _βk_ [1] [with all the other parameters remaining at their]
original values. The arc gradient calculated in this way is not zero or
undefined, and provides information on the direction of rise. Nevertheless, the A-R simulated probability is difficult because of its inherent
lack of a slope, coupled with the possibility of it being zero.


**5.6.2** **Smoothed A-R simulators**


One way to mitigate the difficulties with the A-R simulator is to replace the 0-1 accept/reject indicator with a smooth, strictly positive
function. The simulation starts the same as with A-R, by taking draws


_5.6. SIMULATION OF THE CHOICE PROBABILITIES_ 137


of the random terms and calculating the utility of each alternative for
each draw: _Unj_ _[r]_ [. Then instead of determining whether alternative] _[ i]_ [ has]
the highest utility (that is, instead of calculating the indicator function
_I_ _[r]_ ), the simulated utilities _Unj_ _[r]_ _[∀]_ _[j]_ [ are entered into a function. Any]
function can be used for simulating _Pni_ as long as it rises when _Uni_ _[r]_
rises, declines when _Unj_ _[r]_ [rises, is strictly positive, and has defined first]
and second derivatives with respect to _Unj_ _[r]_ _[∀]_ _[j]_ [. A function that is par-]
ticularly convenient is the logit function, as suggested by McFadden
(1989). Use of this function gives the “logit smoothed A-R simulator.”
The simulator is implemented in the following steps, which are the
same as with the A-R simulator except for step 3.


1. Draw a value of the J-dimensional vector of errors, _εn_, from a
normal density with zero mean and covariance Ω. Label the draw
_ε_ _[r]_ _n_ [with] _[ r]_ [ = 1 and the elements of the draw as] _[ ε]_ _n_ _[r]_ 1 _[, . . ., ε][r]_ _nJ_ [.]


2. Using these values of the errors, calculate the utility that each
alternative obtains with these errors. That is, calculate _Unj_ _[r]_ [=]
_Vnj_ + _ε_ _[r]_ _nj_ _[∀]_ _[j]_ [.]


3. Put these utilities into the logit formula. That is, calculate


_e_ _[U]_ _ni_ _[r]_ _[/λ]_
_Sr_ = ~~�~~
_nj_ _[/λ]_
_j_ _[e][U]_ ~~_[r]_~~


where _λ >_ 0 is a scale factor specified by the researcher and
discussed below.


4. Repeat steps 1-3 many times. Label the number of repetitions
(including the first) as R, such that r takes values of 1 through
R.


5. The simulated probability is the number of accepts divided by
the number of repetitions: _P_ [ˇ] _ni_ = _R_ [1]    - _Rr_ =1 _[S][r]_ [.]

Since _S_ _[r]_ _>_ 0 for all finite values of _Unj_ _[r]_ [, the simulated probability]
is strictly positive for any draws of the errors. It rises with _Uni_ _[r]_ [and]
declines when _Unj_ _[r]_ _[j][ ̸]_ [=] _[ i]_ [ rises. It is smooth (twice differentiable) since]
the logit formula itself is smooth.
The logit-smoothed A-R simulator can be applied to any choice
model, simply by simulating the utilities under any distributional assumptions about the errors and then inserting the utilities into the


138 _CHAPTER 5. PROBIT_


logit formula. When applied to probit, Ben-Akiva and Bolduc (1996)
have called it “logit-kernel probit.”
The scale factor _λ_ determines the degree of smoothing. As _λ →_ 0,
_S_ _[r]_ approaches the indicator function _I_ _[r]_ . Figure 5.2 illustrates the situation for a two-alternative case. For a given draw of _ε_ _[r]_ _n_ [, the utility of]
the two alternatives is calculated. Consider the simulated probability
for alternative 1. With A-R, the 0-1 indicator function is zero if _Un_ _[r]_ 1
is below _Un_ _[r]_ 2 [and one if] _[ U]_ _n_ _[r]_ 1 [exceeds] _[ U]_ _n_ _[r]_ 2 [. With logit-smoothing, the]
step function is replaced by a smooth sigmoid curve. The factor _λ_ determines the proximity of the sigmoid to the 0-1 indicator. Lowering
_λ_ increases the scale of the utilities when they enter the logit function
(since the utilities are divided by _λ_ .) Increasing the scale of utility
increases the absolute difference between the two utilities. The logit
formula gives probabilities that are closer to zero or one when the difference in utilities is larger. The logit-smoothed _S_ _[r]_ therefore becomes
closer to the step function as _λ_ becomes closer to zero.


_r_
_Pn1_


1


_r_



0


|Col1|Logit<br>with h<br>Logit smoot<br>with λ close<br>0-1 Indicator, I|Col3|
|---|---|---|
|||0-1 Indicator,_I_<br>Logit<br>with h<br>Logit smoot<br>withλ close|



_Un2r_ _Un1r_


Figure 5.2: A-R smoother.



The researcher needs to set the value of _λ_ . A lower value of _λ_ makes
the logit-smoother a better approximation to the indicator function.
However, this fact is a double-edge sword: if the logit-smoother approximates the indicator function too well, the numerical difficulties of
using the unsmoothed A-R simulator will simply be reproduced in the


_5.6. SIMULATION OF THE CHOICE PROBABILITIES_ 139


logit-smoothed simulator. The researcher wants to set _λ_ low enough
to obtain a good approximation but not so low as to re-introduce numerical difficulties. There is little guidance on the appropriate level of
_λ_ . Perhaps the best approach is for the researcher to experiment with
different _λ_ ’s. The same draws of _εn_ should be used with each different
_λ_, so as to assure that differences in results are due to the change in
the _λ_ rather than to differences in the draws.
McFadden (1989) describes other smoothing functions. For all of
them, the researcher must specify the degree of smoothing. An advantage of the logit smoother is its simplicity. Also, we will see in Chapter
6 that the logit-smoother applied to a probit or any other model constitutes a type of mixed logit specification. That is, instead of seeing
the logit smoother as providing an approximation that has no behavioral relation to the model (simply serving a numerical purpose), the
logit smoother can be seen as arising from a particular type of error
structure in the behavioral model itself. Under this interpretation, the
logit formula applied to simulated utilities is not an approximation but
actually represents the true model.


**5.6.3** **GHK simulator**


The most widely used probit simulator is called GHK, after Geweke
(1989, 1991), Hajivassiliou (as reported in Hajivassiliou and McFadden,
1998), and Keane (1990 1994), who developed the procedure. In a
comparison of numerous probit simulators, Hajivassiliou et al. (1996)
found GHK to be the most accurate in the settings that they examined.
Geweke, Keane and Runkle (1994) found the GHK simulator works
better than smoothed A-R. Experience has confirmed its usefulness
and relative accuracy (e.g., Borsch-Supan and Hajivassiliou (1993)).
The GHK simulator operates on utility differences. The simulation
of probability _Pni_ starts by subtracting the utility of alternative _i_ from
each other alternative’s utility. Importantly, the utility of a different
alternative is subtracted depending on which probability is being simulated: for _Pni_, _Uni_ is subtracted from the other utilities, while for
_Pnj_, _Unj_ is subtracted. This fact is critical to the implementation of
the procedure.
I will explain the GHK procedure first in terms of a three-alternative
case, since that situation can be depicted graphically in two dimensions
for utility differences. I will then describe the procedure in general for


140 _CHAPTER 5. PROBIT_


any number of alternatives. Bolduc (1993, 1999 provide an excellent
alternative description of the procedure, along with methods to simulate the analytic derivatives of the probit probabilities. Keane (1994)
provides a description of the use of GHK for transition probabilities.


**Three alternatives**


We start with a specification of the behavioral model in utilities: _Unj_ =
_Vnj_ + _εnj, j_ = 1 _,_ 2 _,_ 3 _._ The vector _ε_ _[′]_ _n_ [=] _[ ⟨][ε][n]_ [1] _[, ε][n]_ [2] _[, ε][n]_ [3] _[⟩∼]_ _[N]_ [(0] _[,]_ [ Ω). We]
assume that the reseacher has normalized the model for scale and level
such that the parameters that enter Ωare identified. Also, Ωcan be
a parametric function of data, as with random taste variation, though
we do not show this dependence in our notation.
Suppose we want to simulate the probability of the first alternative,
_Pn_ 1. We re-express the model in utility differences by subtracting the
utility of alternative 1:


( _Unj −_ _Un_ 1) = ( _Vnj −_ _Vn_ 1) + ( _εnj −_ _εn_ 1)
_U_ ˜ _nj_ 1 = _V_ ˜ _nj_ 1 + ˜ _εnj_ 1

for _j_ = 2 _,_ 3 _._ The vector ˜ _ε_ _[′]_ _n_ 1 [=] _[ ⟨][ε]_ [˜] _[n]_ [21] _[,]_ [ ˜] _[ε][n]_ [31] _[⟩]_ [is distributed] _[ N]_ [(0] _[,]_ [ ˜Ω][1][) where]
˜Ω1 is derived from Ω.
We take one more transformation to make the model more convenient for simulation. In particular, let _L_ 1 be the Choleski factor of Ω [˜] 1.
Since Ω [˜] 1 is 2 _×_ 2 in our current illustration, _L_ 1 is a lower-triangular
matrix that takes the form:







_L_ 1 =




_caa_ 0
_cab_ _cbb_



_._



Using this Choleski factor, the original error differences, which are correlated, can be re-written as linear functions of _uncorrelated_ standard
normal deviates:


_ε_ ˜ _n_ 21 = _caaη_ 1
_ε_ ˜ _n_ 31 = _cabη_ 1 + _cbbη_ 2


where _η_ 1 and _η_ 2 are iid _N_ (0 _,_ 1). The error differences ˜ _εn_ 21 and ˜ _εn_ 31
are correlated because both of them depend on _η_ 1. With this way of
expressing the error differences, the utility differences can be written:


_U_ ˜ _n_ 21 = _V_ ˜ _n_ 21 + _caaη_ 1
_U_ ˜ _n_ 31 = _V_ ˜ _n_ 31 + _cabη_ 1 + _cbbη_ 2 _._


