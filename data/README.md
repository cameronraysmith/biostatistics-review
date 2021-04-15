# Book website

[Bayesian Biostatistics website](https://www.wiley.com/go/bayesian_methods_biostatistics)

https://media.wiley.com/product_ancillary/32/04700182/DOWNLOAD/DataLesaffreLawson.rar
https://media.wiley.com/product_ancillary/32/04700182/DOWNLOAD/Programs_Lesaffre%20Lawson_Part_1.zip
https://media.wiley.com/product_ancillary/32/04700182/DOWNLOAD/Programs_Lesaffre%20Lawson_Part_2.zip
https://media.wiley.com/product_ancillary/32/04700182/DOWNLOAD/BayesianBiostatistics-errata_2015.pdf
https://media.wiley.com/product_ancillary/32/04700182/DOWNLOAD/ProgramsBayesianBiostatistics.rar

# Data sets and section references

## Treatment of toenail fungus

See De Backer et al. 1996

> De Backer M, De Keyser P, De Vroey C and Lesaffre E 1996 A 12-week treatment for dermatophyte toe onycholysis: terbinafine 250 mg/day vs. itraconazole 200 mg/day – a double-blind comparative trial. British Journal of Dermatology 134, 16–17.

### Example listing

- Example I.1:   Evaluation of two oral treatments for toenail infection using the frequentist approach p. 4
- Example I.2:   P-value p. 5
- Example I.6:   95% confidence interval p. 8
- Example I.12:  Bayesian analysis p. 18
- Example IX.12: Bayesian linear mixed model p. 246
- Example IX.14: Bayesian logistic random intercept model p. 249
- Example IX.15: Bayesian logistic random intercept and slope model p. 250
- Example IX.19: Exploring random effects in Bayesian linear mixed model
- Example X.22:  Checking normality of the random intercept in a logistic random intercept model

### Data files

```
├── toenailb.sas7bdat
├── toenailb.txt
├── toenail.tsv
└── toenail.txt
```

```
├── ALP.txt
├── caries.txt
├── DataLesaffreLawson.rar
├── diet2.txt
├── diet.txt
├── dmft.txt
├── efron.sas7bdat
├── efron.txt
├── glioma.txt
├── IBBENS.xls
├── jimma.txt
├── lipcancer.txt
├── misclassification.csv
├── misclassification.sas7bdat
├── osteopmult.txt
├── osteoporosismultiple.txt
├── osteop.txt
├── osteo.sas7bdat
├── potthoffroy.txt
├── reach.txt
├── README.md
├── stm.sas7bdat
├── stm.txt
```

# Contents overview

## I. Relation between Bayesian inference and NHST

- 01: significance test
- 02: Bayesian inference
- 03: Posterior summaries and predictive distributions
- 04: Extension to multivariate distributions
- 05: Prior elicitation
- 06: Gibbs and MH MCMC via example
- 07: Assessing and accelerating MCMC convergence
- 08: Review of software circa time of publication (BUGS, SAS, JAGS)

## II. Probabilistic modelling

- 09: Hierarchical modelling
- 10: Model building and assessment
- 11: Bayesian variable selection

## III. Areas of application

- 12: Preclinical testing
- 13: Measurement error and misclassification
- 14: Bayesian survival analysis
- 15: Bayesian longitudinal analysis
- 16: Bayesian spatial analysis
- 17: Review of topics not covered

# Detailed contents

TABLE OF CONTENTS
Preface xiii
Notation, terminology and some guidance for reading the book xvii

## Part I BASIC CONCEPTS IN BAYESIAN METHODS

### 1 Modes of statistical inference 3
1.1 The frequentist approach: A critical reflection 4
1.2 Statistical inference based on the likelihood function 10
1.3 The Bayesian approach: Some basic ideas 14
1.4 Outlook 18

### 2 Bayes theorem: Computing the posterior distribution 20
2.1 Introduction 20
2.2 Bayes theorem – the binary version 20
2.3 Probability in a Bayesian context 21
2.4 Bayes theorem – the categorical version 22
2.5 Bayes theorem – the continuous version 23
2.6 The binomial case 24
2.7 The Gaussian case 30
2.8 The Poisson case 36
2.9 The prior and posterior distribution of h(θ) 40
2.10 Bayesian versus likelihood approach 40
2.11 Bayesian versus frequentist approach 41
2.12 The different modes of the Bayesian approach 41
2.13 An historical note on the Bayesian approach 42
2.14 Closing remarks 44

### 3 Introduction to Bayesian inference 46
3.1 Introduction 46
3.2 Summarizing the posterior by probabilities 46
3.3 Posterior summary measures 47
3.4 Predictive distributions 51
3.5 Exchangeability 58
3.6 A normal approximation to the posterior 60
3.7 Numerical techniques to determine the posterior 63
3.8 Bayesian hypothesis testing 72
3.9 Closing remarks 78

### 4 More than one parameter 82
4.1 Introduction 82
4.2 Joint versus marginal posterior inference 83
4.3 The normal distribution with μ and σ2 unknown 83
4.4 Multivariate distributions 89
4.5 Frequentist properties of Bayesian inference 92
4.6 Sampling from the posterior distribution: The Method of Composition 93
4.7 Bayesian linear regression models 96
4.8 Bayesian generalized linear models 101
4.9 More complex regression models 102
4.10 Closing remarks 102

### 5 Choosing the prior distribution 104
5.1 Introduction 104
5.2 The sequential use of Bayes theorem 104
5.3 Conjugate prior distributions 106
5.4 Noninformative prior distributions 113
5.5 Informative prior distributions 121
5.6 Prior distributions for regression models 129
5.7 Modeling priors 134
5.8 Other regression models 136
5.9 Closing remarks 136

### 6 Markov chain Monte Carlo sampling 139
6.1 Introduction 139
6.2 The Gibbs sampler 140
6.3 The Metropolis(–Hastings) algorithm 154
6.4 Justification of the MCMC approaches∗ 162
6.5 Choice of the sampler 165
6.6 The Reversible Jump MCMC algorithm∗ 168
6.7 Closing remarks 172

### 7 Assessing and improving convergence of the Markov chain 175
7.1 Introduction 175
7.2 Assessing convergence of a Markov chain 176
7.3 Accelerating convergence 189
7.4 Practical guidelines for assessing and accelerating convergence 194
7.5 Data augmentation 195
7.6 Closing remarks 200

### 8 Software 202
8.1 WinBUGS and related software 202
8.2 Bayesian analysis using SAS 215
8.3 Additional Bayesian software and comparisons 221
8.4 Closing remarks 222

## Part II BAYESIAN TOOLS FOR STATISTICAL MODELING

### 9 Hierarchical models 227
9.1 Introduction 227
9.2 The Poisson-gamma hierarchical model 228
9.3 Full versus empirical Bayesian approach 238
9.4 Gaussian hierarchical models 240
9.5 Mixed models 244
9.6 Propriety of the posterior 260
9.7 Assessing and accelerating convergence 261
9.8 Comparison of Bayesian and frequentist hierarchical models 263
9.9 Closing remarks 265

### 10 Model building and assessment 267
10.1 Introduction 267
10.2 Measures for model selection 268
10.3 Model checking 288
10.4 Closing remarks 316

### 11 Variable selection 319
11.1 Introduction 319
11.2 Classical variable selection 320
11.3 Bayesian variable selection: Concepts and questions 325
11.4 Introduction to Bayesian variable selection 326
11.5 Variable selection based on Zellner’s g-prior 333
11.6 Variable selection based on Reversible Jump Markov chain Monte Carlo 336
11.7 Spike and slab priors 339
11.8 Bayesian regularization 345
11.9 The many regressors case 351
11.10 Bayesian model selection 355
11.11 Bayesian model averaging 357
11.12 Closing remarks 359

## Part III BAYESIAN METHODS IN PRACTICAL APPLICATIONS

### 12 Bioassay 365
12.1 Bioassay essentials 365
12.2 A generic in vitro example 369
12.3 Ames/Salmonella mutagenic assay 371
12.4 Mouse lymphoma assay (L5178Y TK+/−) 373
12.5 Closing remarks 374

### 13 Measurement error 375
13.1 Continuous measurement error 375
13.2 Discrete measurement error 382
13.3 Closing remarks 389

### 14 Survival analysis 390
14.1 Basic terminology 390
14.2 The Bayesian model formulation 394
14.3 Examples 397
14.4 Closing remarks 406

### 15 Longitudinal analysis 407
15.1 Fixed time periods 407
15.2 Random event times 417
15.3 Dealing with missing data 420
15.4 Joint modeling of longitudinal and survival responses 424
15.5 Closing remarks 429

### 16 Spatial applications: Disease mapping and image analysis 430
16.1 Introduction 430
16.2 Disease mapping 430
16.3 Image analysis 444

### 17 Final chapter 456
17.1 What this book covered 456
17.2 Additional Bayesian developments 456
17.3 Alternative reading 459

## Appendix: Distributions 460
A.1 Introduction 460
A.2 Continuous univariate distributions 461
A.3 Discrete univariate distributions 477
A.4 Multivariate distributions 481

References 484
Index 509