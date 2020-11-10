# On the history of uncertainty measures: The standard deviation

*Update (Nov. 10th, 2020): I started this project in 2016, with the hope that it would take me less than 2 years to complete. To really write this piece would mean to (re)visit librairies I went to two years ago - something that is difficult to do in the context of a pandemic. I am shelving this work for now.*

*If you are interested in the relationship and history of standard deviation as a measure of volatility, please feel welcome to get in touch by email. You will find a current one on the contact page.*

*You may read the [first draft of this project](stdev_draft.html)*

*Not included here is the 30-or-so pages of notes that I have compiled for this project.*

## Abstract

This fieldbook is meant to be the backbone of two essays on the relationship of standard deviation and volatility. The first essay was going to be on the history of the standard deviation as an uncertainty measure and on the evolution of volatility as a concept; the second one, on contemporary use of the standard deviation as a measure of volatility.

Questions I have been asking myself includes:

1. When did humanity started to contemplate taking measurements of uncertainty?

2. What were the first measures of uncertainty?

3. When did we first use the standard deviation as a measure of uncertainty?

4. When did we start calling standard deviation by this name?

DISCLAIMER: I am not an historian.

## Table of contents

## Context

While working on my master thesis in financial engineering, I started asking myself questions about the nature of volatility, and how well it is measured by contemporary metrics. This family of questions brought me to consider the history of the standard deviation, for itself and as a measure of volatility, trying to find when were born the first occurences of these technical terms. This current essay is about the history of the standard deviation.

The [complete list of references](mybibfinish.html) might be of interest to you.

## What is volatility 

Volatility in finance can be roughly understood as uncertainty: how much things might change, how much we expect them to change or not. This is not a strict, thorough definition.

## What is the standard deviation

The standard deviation is a precise term in statistics that roughly measure how widely dispersed a dataset is around its mean.

# The fieldbook

This version of the fieldbook is a snapshot of where I last left the work - it is not complete. It is limited by time and resources available, and the fact that the only languages I can currently read are French and English.


## Before 1700

According to our research, the main driver of error measurements before 1700 was the study of the stars locations, and in a broader way, astronomy.

### Ptolemy

In *Histoire de la Statistique* (1990), Droesbeke and Tassi underlines that around Ptolémé's time, "le fait de posséder plusieurs valeurs observées ont conduit ces astronomes à proposer des valeurs uniques accompagnées de mesure de variation basées, semble-t-il, sur l'étendue des observations. Le choix systématique d'une moyenne ou d'une médiane n'était cependant pas encore d'actualité." (our translation: it is the fact that astronomers found multiple observed values that drove them to propose unique values coupled with variation measurements based on the scope of observations. There was no systematic choice between using an average or a median yet.)

It would be interesting to see what are these uncertainty measures based on the scope of observations, and to try to figure out how related they are to our contemporary definition of standard deviation. *More research is needed*.

### Galileo

In the same *Histoire de la statistique* (1990), it is noted that Galileo was interested in finding ways to correct measurement errors, "juste assez pour ôter les observations de l'impossible et les remettre dans le possible." (just enough to change impossible observations in possible ones.) 

Once again, there is not precise definition about what were these ways. *More research is needed*.

### 1700

The 18th century brings forward a broader and deeper discussion of statistics and probabilities. We are now interested in uncertainty for itself, and we are moving forward from astronomy. By the end of this century, humanity will have considered at least one measure that we can call *standard deviation*. It is not our goal to establish who was the first person to exactly describe the standard deviation as we now know it; we are more interested in drawing a fair timeline of known intellectual developments surrounding the measurement of uncertainty.

### Bernoulli

In 1713, Jacob Bernoulli's nephew publishes post-humously his book, *Ars Conjectandi*. Stigler notes in *The History of Statistics: The Measurement of Uncertainty before 1900* (1986) that it was "perhaps the first time [that] a mathematical approach to the measurement of uncertainty had been developed. Bernoulli had not shown merely that, qualitattively, the greater the number of observations the less the uncertainty in the result, he had shown how to this statement could be quantified." 

*More research is needed*: what exactly were these measurements, in mathematical terms ?

### De Moivre

In 1718, de Moivre publishes *The Doctrine of Chances*.  Abbott notes in *Mathematicians* (1985) that he seemed "to have been aware of the standard deviation paramater ( \sigma ), although he did not specify it."

In 1730, de Moivre publishes *Miscellanea Analytica*. According to Berstein in *Against the gods: the remarkable story of risk* (1998), it is in this book that "de Moivre suggested the structure of the normal distribution", and that "the shape of de Moivre's curve enabled him to calculate a statistical measure of its dispersion around the mean." He notes that it is the one now known as the standard deviation.

*More research is needed*: what exactly is written in the original work ?

Page 490 of Hald's "A history of probability and statistics and their applications before 1750" (1990), we can see that De Moivre correctly identifies the deviation *d* as being $\sqrt(npq)$ but he doesn't derive this result as being variance. 

### Simpson

The derivation of the way to calculate the standard deviation is closely linked to measures of central tendency, like the average or the mean, and the median.

In 1755, Stigler (1986) brings the light on Thomas Simpson' 1755 work, *On the advantage of taking the mean of a number of observations, in practical astronomy": " He was able to focus his attention on the mean *error* rather than on the mean *observation*. Even though the position of the body observed might be considered unknown, the distribution of errors was, for Simpson, known." 

According to Droesbeke & Tassi (1990), Simpson allows us to focus on  "la loi de probabilité des erreurs (différence entre la vraie valeur d'une quantité et les mesures fournissant des valeurs observées.) Elle fut introduite dans le but de montrer l'utilité de prendre la moyenne arithmétique de valeurs observées pour "estimer" un paramètre." (Our translation: "the probability of errors law, the difference between the real value of a quantity and the measures giving the observed values. It was introduced with the goal of showing how useful it is to take the arithmetic mean of observed values in order to estimate a parameter." )

### Lambert

In 1760, Lambert publishes *Photometria*, in which density curves are discussed. Drosbeke & Tassi (1990) put forward the fact that it is in this work préface that the expression "error theory" (*Die Theorie der Fehler*) is introduced. 

*More research is needed* to establish how close to our main uncertainty measure is Lambert's error theory.

### Laplace

It is in 1774 that Laplace proposes a distribution  where the domain is the set of real numbers, states Droesbeke & Tassi (1990): "this distribution, called the double exponentielle, is also known as Laplace's first law of error distributions. This distribution considers the absolute value of the difference between each observation and the median. Laplace would later considers the difference between each observation and the average, to the power of two." (our translation)

### 1800

It is during the 19th century that we can start tracing a multitude of uncertainty measures. In Droesbeke & Tassi (1990), a few are named: "le *module* (C=$\sigma *\sqrt(2)$), l'erreur moyenne ($C/ \pi$), le carré moyen ($\sigma^2$)...". 

But first, let's start with a giant.

### Gauss

In 1809, Gauss derives the normal density. Stigler (1986) notes that "no scheme was presented to determine the unknown precision of *h* of a single measurement." An important point to our study of uncertainty measurement is made by Schaaf (1964): "it turns out, among other things, that the arithmetic mean has the property that the sum of the squares of the deviations is less than when these  are measurement from the mean, than when they are measured from any other reference point." We will come back to this later, in the essay on understanding volatility measurements.

It is in 1816, seven years later, it is explained in Droesbeke & Tassi (1990) that Gauss will "propose to use the following expression as a way to measure the variations of measurement errors in astronomy:

$$ \epsilon_k = \left( \frac{1}{n} \sum_{i=1}^n x_i^k \right) ^{\frac{1}{k}}.  $$

Here, $x_i$ is the absolute value of the difference between the i-th observation and the arithmetic mean; $n$ is the number of observations; $k$ is an integer. Drosbeke and Tassi (1990) notes that while Gauss prefered to use $k=2$, Laplace prefered $k=1$.

In "Annotated readings in the history of statistics", David & Edwards (2001) notes that "Gauss goes on to show that, for large $m$, the true value of $h$ [the error law constant previously considered] lies with probability 1/2 in :

$$ \hat{h} ( 1 - \rho m^{-1\/2}), \hat{h}(1 + \rho m^{-1/2})$$ 

In modern terminology, [it] is a large-sample 50\% Bayesian confidence interval corresponding to a uniform prior, and hence is also an ordinary large-sample CI [confidence interval]. "

Given that computers have yet to be invented, one thing that is considered important is ease of calculation: "ease of calculation is so important that Gauss even considers m = med(abs(x_1)), the median absolute deviation (MAD)" (David & Edwards, (2001)). Some modern concerns are not yet of interest to Gauss or his contemporaries: "that $S_1$ [in this article, \epsiilon_1] and especially $M$ have the advantage of greater robustness than $\sqrt(S_2)$ does not enter at this early stage." (David & Edwards, (2001))

David & Edwards (2001) then cites Gauss directly : " It is not at all necessary to know the value of $h$ in order to apply the method of least squares to determine the most probable values of those quantities [parameters] on which the observations depend. Also, the ratio fo the accuracy of the results to the accuracy of the observations does not depend on $h$. However, knowledge of its value is in itself interesting and instructive, and I will therefore show how we can arrive at such knowledge through the observations themselves."

### Laplace

An important fact about the standard deviation is that it is the square of the variance, which can be calculated in a straightforward way :

$$ Var(x) = E[x^2] - E[x]^2.$$

As a way to gain knowledge about how the standard deviation was computed, we spent some time researching how and when this previous formula was first discovered. Although *more research is needed*, Laplace seems to be one of the first to consider calculating variance this way. We can see this formula in Laplace (1812), and Stigler (1986) states that Laplace tried to measure variance. 

### Encke

Publication of *Uber die Methode der kleinstein Quadrate* (1832), where he demonstrates that the variance is the mean of the the squares minus the square of the mean:

$$ Var(x) = E[x^2] - E[x]^2.$$

### Jevons

In 1874, Jevons introduces the geometric mean and the harmomic mean, but does not seem to use them for standard deviation calculations purposes.

### Edgeworth 

In 1885, Edgeworth (from the Edgeworth box fame) publishes *Methods of statistics* in the Jubilee Volumn of Statistics. Stigler explains his significance test in the following way:

        Given two "means" (which could be either medians of other estimates), first estimate their fluctuations, a term Edgeworth invented to mean the modulus-squared, or, in modern terminology, twice the variance."

Concretely, this gives us:

$$ C^2 = 2 * \sum (X_i - \bar{X}) \ n. $$

Edgeworth defense was based, according to Stigler, on the "grunds that it maximized the posterior density, while *(n-1)* does not appear to correspond to the maximum of anything in particular".        

We will come back to Edgeworth works when we discuss the link between the history of the standard deviation and the history of the volatility concept.

### Pearson

Pearson will build on Edgworth works in the following way: he will, in 1893, coin the term of "standard deviation", after having initially called it "standard divergence".

According to Stigler, "the genius of Person's choice of a standard was his recognition that accurcay would be greatest if emphasis were put upon the stage of routine calculation, even at some cost in "theoretical" simplicity".

### Yule

We are going to end our study of the 1800's with this simple fact: Yule's introduction of the term *standard error* was made in 1897. 


## References

### Mentionned in the fieldbook

ABBOTT, David (general editor), *Mathematicians*, Blond Educational, 1985.

BERSTEIN, Peter L., *Against the gods : the remarkable story of risk*, John Wiley &
Sons. 1998.

BERTRAND, J. (1855) Méthode des moindres carrés. Mémoire sur la combinaison des observations

DAVID, H.A. & EDWARDS, A.W.F., *Annotated readings in the history of statistics*, Springer, 2001.

DROESBEKE, Jean-Jacques & TASSI, Philippe, *Histoire de la statistique*, Que sais-je ?, 1990.

HALD, Anders, *A history of probability and statistics and their applications before
1750*, Wiley 1990.

LAPLACE, Pierre-Simon, Théorie Analytique des Probabilités, 1812.

SCHAAF, William L., *Carl Friedrich Gauss, prince of Mathematicians*, 1964.

STIGLER, Stephen M. , *The History of Statistics : The Measurement of Uncertainty
before 1900*, The Belknap Press of Harvard University Press,1986 .

WALKER, Helen. *Studies in the History of Statistical Method*, 1929.


[Complete list of references](mybibfinish.html)
