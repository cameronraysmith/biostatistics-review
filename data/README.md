# Book metadata

- [website](https://www.wiley.com/go/bayesian_methods_biostatistics)
- [data](https://media.wiley.com/product_ancillary/32/04700182/DOWNLOAD/DataLesaffreLawson.rar)
- [BUGS programs 1](https://media.wiley.com/product_ancillary/32/04700182/DOWNLOAD/Programs_Lesaffre%20Lawson_Part_1.zip) | [BUGS programs 2](https://media.wiley.com/product_ancillary/32/04700182/DOWNLOAD/Programs_Lesaffre%20Lawson_Part_2.zip) | [BUGS programs all](https://media.wiley.com/product_ancillary/32/04700182/DOWNLOAD/ProgramsBayesianBiostatistics.rar)
- [errata](https://media.wiley.com/product_ancillary/32/04700182/DOWNLOAD/BayesianBiostatistics-errata_2015.pdf)

# Reference to examples and associated data sets

## Uncategorized

### Example listing
- Example V.1: Ames/Salmonella mutagenic assay analysis
- Example V.6: cysticercosis study estimating prevalence in absence of a gold standard p. 124
- Example V.7: skeptical prior in phase III randomized trial p. 127
- Example V.8: skeptical prior in lipid-lowering RCT p. 128
- Example V.9: enthusiastic prior in lipid-lowering RCT p. 129
- Example VI.4: finding the change point using Gibbs sampling in British coal mining disasters data
- Example VII.6: Genetic linkage model estimating the recombination fraction using the data augmentation approach p. 196
- Example VII.7: Cysticercosis study: estimating the prevalence in the absence of a gold standard (ref back to V.6) p. 196
- Example IX.18: arteriosclerosis study: reperfusion models after femoral artery occlusion
- Example X.8: Potthoff and Roy growth-curve study model seelctions using $p_D$ and DIC
- Example X.11: Linkage study in genetics with negative $p_D$s p. 284
- Example X.18: arteriosclerosis study: detection of influential observations p. 298
- Example XI.11: Glioma study: BVS when $d \lt n$
- Example 13.2.2.1: The IRAS multicenter study Liese et al 2004
- Example 14.3.1: Moreau et al 1985 gastric cancer study analysed by Terry Therneau in Modeling Survival Data: Extending the Cox Model
- Example 14.3.2: Prostate cancer in Lousiana SEER registry data analysed via a spatial AFT model

### Data files
```
├── glioma.txt
├── jimma.txt
├── misclassification.csv
├── misclassification.sas7bdat
├── potthoffroy.txt
├── stm.sas7bdat
├── stm.txt
```


## General topics for statistical modelling

### Example listing
- Example I.7:  Surgery experiment to illustrate likelihood functions
- Example I.8:  Another surgery experiment: the stopping rule
- Example I.9:  Bayesian reasoning in daily life
- Example I.10: Sensitivity, specificity, prevalence, and their relation to predictive values
- Example I.11: Bayesian interpretation of published research findings
- Example III.14: credible intervals in Bayesian hypothesis testing (cross-over study)
- Example III.15: Bayes factor (cross-over study)
- Example III.16: Illustration of Lindley's paradox
- Example V.4: data-translated likelihood (DTL) principle applied to normal likelihood in scale given location
- Example V.10: computational difficulties in binary response models p. 135
- Example VI.2: Sampling from a discrete x continuous distribution
- Example VI.6: Slice sampling the normal density p. 154
- Example VII.5: effect of reparametrization on convergence
- Example VII.9: MCMC approaches to probit regression p. 200
- Example X.4: AIC for a linear regression model p. 275
- Example X.5: conditional and marginal likelihood of a linear mixed model p. 277
- Example X.6: effective degrees of freedom of a linear mixed model


See Wikipedia for a brief review of [Lindley's paradox](https://en.wikipedia.org/wiki/Lindley%27s_paradox):

> Lindley's paradox is a counterintuitive situation in statistics in which the Bayesian and frequentist approaches to a hypothesis testing problem give different results for certain choices of the prior distribution. The problem of the disagreement between the two approaches was discussed in Harold Jeffreys' 1939 textbook; it became known as Lindley's paradox after Dennis Lindley called the disagreement a paradox in a 1957 paper.


## RCT of oral treatments for toenail fungus

See De Backer et al. 1996

> De Backer M, De Keyser P, De Vroey C and Lesaffre E 1996 A 12-week treatment for dermatophyte toe onycholysis: terbinafine 250 mg/day vs. itraconazole 200 mg/day – a double-blind comparative trial. British Journal of Dermatology 134, 16–17.

### Example listing

- Example I.1:   evaluation of two oral treatments for toenail infection using the frequentist approach p. 4
- Example I.2:   P-value p. 5
- Example I.3:   accounting for interim analyses in a RCT p. 5
- Example I.6:   95% confidence interval p. 8
- Example I.12:  Bayesian analysis p. 18
- Example IX.12: Bayesian linear mixed model p. 246
- Figure 9.12: graphical representation of the BLMM
- Example IX.14: Bayesian logistic random intercept model p. 249
- Example IX.15: Bayesian logistic random intercept and slope model p. 250
- Example IX.19: exploring random effects in Bayesian linear mixed model p. 256
- Example X.22:  checking normality of the random intercept in a logistic random intercept model p. 306
- Example X.23:  Illustration of Steinbakk and Storvik p. 307


### Data files

```
├── toenailb.sas7bdat
├── toenailb.txt
├── toenail.tsv
└── toenail.txt
```

## Impact of chemotherapy on development of leukemia in Hodgkin's lymphoma survivors

See Kaldor et al. 1990

> Kaldor JM, Day NE, Clarke EA, Van Leeuwen FE, Henry-Amar M, Fiorentino MV, et al. Leukemia following Hodgkin’s disease. N Engl J Med. 1990;322: 7–13. doi:10.1056/NEJM199001043220102

### Example listing

- Example I.4:  case-control study: Illustration of sample space p. 6
- Example I.5: Merseyside registry results: small sample size and prior information p. 8
- Example III.9: posterior inference using normal approximations p. 60
- Example IV.4: reanalysis of III.9 p. 92

### Data files


## Stroke studies (ECASS series)

### Papers

- Donnan, 1996
- Hacke,  1995 (ECASS 1)
- Hacke,  1998 (ECASS 2)
- [Hacke,  2008 (ECASS 3)](https://www.wikijournalclub.org/wiki/ECASS_III)
- Amiri,  2016 (ECASS 4)

> Hacke W, Kaste M, Bluhmki E, Brozman M, Dávalos A, Guidetti D, et al. Thrombolysis with alteplase 3 to 4.5 hours after acute ischemic stroke. N Engl J Med. 2008;359: 1317–1329. doi:10.1056/NEJMoa0804656
>
> Amiri H, Bluhmki E, Bendszus M, Eschenfelder CC, Donnan GA, Leys D, et al. European Cooperative Acute Stroke Study-4: Extending the time for thrombolysis in emergency neurological deficits ECASS-4: ExTEND. Int J Stroke. 2016;11: 260–267. doi:10.1177/1747493015620805

The clinical question addressed in ECASS 3 according to [wikijournalclub](https://www.wikijournalclub.org/wiki/ECASS_III) is:
> In patients with acute ischemic stroke, does the administration of alteplase, a tissue plasminogen activator (tPA), reduce disability at 3 months?

### Example listing

- Example II.1:  monitoring safety of a thrombolytic drug administered for ischemic stroke p. 24
- Example II.4:  posterior distribution of $\log(\theta)$ p. 40
- Example III.1: symptomatic intracerebral hemorrhage (SICH) incidence p. 47
- Example III.5: interval estimation of SICH probability p. 51
- Example III.7: predicting SICH incidence in interim analysis p. 56
- Example V.5 prior distribution for the first interim analysis from expert knowledge p. 122


## Dietary study (IBBENS)

> Inter-regional Belgian Bank Employee Nutrition Study (IBBENS) https://pubmed.ncbi.nlm.nih.gov/8194492/

### Example listing

- Example II.2: monitoring dietary behavior in Belgium p. 30
- Example III.3: posterior summary measures p. 49
- Example III.4: interval estimation of dietary intake p. 50
- Example V.2: normal versus $t$-prior p. 109
- Example IX.7: comparing cholesterol intake between subsidiaries in WinBUGS p. 241
- Figure 9.9: graphical representation of the Gaussian hierarchical model p. 242
- Example IX.8: comparing cholesterol intake between subsidiaries with SAS
- Example IX.9: posterior predictive distribution in WinBUGS
- Example IX.10: an empirical Bayes analysis with SAS PROC MIXED
- Example IX.11: comparison of cholesterol intake between subsidiaries corrected for age and gender p. 246
- Example IX.20: choosing a vague proper prior for the level-2 variance p. 258
- Example IX.21: improving convergence p. 263
- Example IX.22: comparison with frequentist estimation
- Example X.10: impact of variability of random effects and scale of response on $p_D$ and DIC p. 283
- Example X.24: estimating the Box-Cox transformation of the response p. 310
- Example X.27: cubic-spline smoothing in a logistic random effects model p. 315


### Data files

```
├── diet2.txt
├── diet.txt
├── IBBENS.xls
```


## Caries study

Vanobbergen et al. 2000

> Vanobbergen J, Martens L, Lesaffre E. The Signal-Tandmobiel project a longitudinal intervention health promotion study in Flanders (Belgium): baseline and first year results. European Journal of. 2000. Available: https://lirias.kuleuven.be/retrieve/1719

### Example listing

- Example II.3: caries in Flanders, Belgium p. 
- Example III.8: PPD for caries experience p. 57
- Example III.10: posterior of mean (dmft-index) p. 63
- Example III.11: posterior distribution for a lognormal prior p. 65
- Example III.12: sampling the posterior distribution p. 66
- Example III.13: sampling the posterior distribution with a lognormal prior p. 70
- Example V.3: approximating the lognormal prior p. 113
- Example VI.9: MCMC for a logistic regression problem p. 166
- Example VI.10: selecting Poisson vs negative binomial using RJMCMC p. 170
- Example VII.8: analysis of interval-censored data p. 198
- Example X.1: choosing between a Poisson and a binomial distribution for the dmft index p. 269
- Example X.2: choosing between three distributions for the dmft index with the Bayes factor
- Example X.3: choosing between three distributions for the dmft index with the pseudo-Bayes factor
- Example X.15: application of posterior predictive ordinate to detect outliers p. 293
- Example 13.2.3.1: missclassification error in scoring caries in the Signal-Tandmobiel study

### Data files
```
├── caries.txt
├── dmft.txt
```

## Serum alkaline phosphatase study

Topal et al 2003

> Topal B, Van de Moortel M, Fieuws S, Vanbeckevoort D, Van Steenbergen W, Aerts R, et al. The value of magnetic resonance cholangiopancreatography in predicting common bile duct stones in patients with gallstone disease. Br J Surg. 2003;90: 42–47. doi:10.1002/bjs.4025

> After having conducted a retrospective study predicting the incidence of common bile duct stones in patients with gallstone disease, Topal et al. (2003) measured serum alkaline phosphatase on a prospective set of 250 ‘healthy’ patients.

### Example listing

- Example III.6: 95% reference interval
- Example IV.1: noninformative prior p. 86
- Example IV.2: conjugate prior p. 88
- Example IV.3: association between smoking and alcohol drinking p. 91
- Example IV.5: sampling the posterior - non-informative prior
- Example IV.6: sampling the posterior - product of informative priors
- Example VI.1: Gibbs sampling the posterior for a non-informative prior p. 141
- Example VI.3: Gibbs sampling the posterior for a semi-conjugate prior p. 144
- Example VI.7: exploring the posterior with the Metropolis algorithm for the non-informative prior p. 156
- Example VI.8: Sampling a $t$-distribution using the independent MH algorithm p. 159
- 

### Data files

```
├── ALP.txt
```

## Osteoporosis

Boonen 1996 examined 245 healthy elderly women to find determinants of osteoporosis.

> Boonen S, Lesaffre E, Dequeker J, Aerssens J, Nijs J, Pelemans W, et al. Relationship between baseline insulin-like growth factor-I (IGF-I) and femoral bone density in women aged over 70 years: potential implications for the prevention of age-related bone loss. J Am Geriatr Soc. 1996;44: 1301–1306. doi:10.1111/j.1532-5415.1996.tb01399.x

### Examples

- Example IV.7: frequentist linear regression (total body bone mineral content, TBBMC, vs BMI)
- Example IV.8: sampling from the posterior using the method of composition
- Example VI.5: exploring the posterior with the Gibbs sampler
- Example VII.1: assessing convergence graphically p. 178
- Example VII.2: assessing convergence using formal diagnostic tests p. 184
- Example VII.3: estimating the Monte Carlo standard error of the posterior mean p. 187
- Example VII.4: accelerating convergence p. 191
- Figure 8.11: graphical model for simple linear regression with response TBBMC and regressor BMI
- Example X.7: $p_D$ and DIC compared to $p$ and AIC p. 279
- Example X.12: predictive evaluation of models p. 288
- Example X.13: detection of outliers p. 291
- Example X.14: cross-validated residuals using WinBUGS p. 292
- Example X.17: detection of influential observations p. 298
- Example X.19: checking distributional assumptions with the posterior-predictive check p. 303
- Example X.25: smoothing the relationship of TBBMC with BMI using cubic splines p. 312
- Example X.26: smoothing the relationship of TBBMC with BMI using B-splines p. 314



### Data files
```
├── osteopmult.txt
├── osteoporosismultiple.txt
├── osteop.txt
├── osteo.sas7bdat
```

## Lip cancer

This is the first example to introduce hierarchical Bayesian models. The first example is a Poisson-gamma model.

- Mohner et al, 1994
> Mohner M, Stabenow R and Eisinger B 1994 Atlas der Krebsinzidenz in der DDR 1961–1989. Berlin: Ullstein Mosby.
https://www.krebsdaten.de/Krebs/EN/Home/homepage_node.html

![Atlas der Krebsinzidenz in der DDR 1961–1989](https://images.booklooker.de/x/016Ou3/Atlas-der-Krebsinzidenz-in-der-DDR-1961-1989.jpg)

- Banuro, 1999
> Banuro F 1999 Relative Risks for Disease Mapping: A New Approach Using a Spatial Mixture Model. Doctoral Thesis: Catholic University of Leuven


### Examples
- Example IX.1: description of the lip cancer study
- Example IX.2: basic modelling assumptions
- Figure 9.2: hierarchical structure in the data
- Example IX.3: example WinBUGS analysis
- Figure 9.3: WinBUGS code for the Poisson-gamma model
- Figure 9.4: graphical representation of the Poisson-gamma model
- Example IX.4: example SAS analysis
- Example IX.5: posterior predictive distribution
- Example IX.6: empirical Bayes analysis
- Example IX.13: Poisson-lognormal model correcting for the percentage of the population engaged in agriculture, forestry, and fisheries (AFF) p. 249
- Example IX.16: correcting for AFF with Albert's model
- Example IX.17: relaxing the normal distribution in the lognormal model
- Example X.16: searching for outliers with PPO, CPO, and DIC diagnostics p. 294
- Example X.20: posterior predictive checking of the Poisson(-gamma) model p. 304
- Example X.21: posterior predictive checking of the Poisson-lognormal model p. 305



### Data files
```
├── lipcancer.txt
```

## Diabetes study

Efron et al, 2004

> Efron B, Hastie T, Johnstone I, Tibshirani R. Least angle regression. aos. 2004;32: 407–499. doi:10.1214/009053604000000067

### Example listing
- Example XI.1: classical automated selection techniques p. 321
- Example XI.2: shrunken regression estimates p. 323
- Example XI.3: Bayesian variable selection (BVS) based on the BIC approximation p. 328
- Example XI.5: BVS based on Occam's window and the $MC^3$ approach
- Example XI.9: BVS using Bayesian LASSO p. 347
- Example XI.10: BVS using extensions of the Bayesian LASSO approach p. 351
- Example XI.13: Bayesian model averaging p. 358


### Data files
```
├── efron.sas7bdat
├── efron.txt
```

## Rheumatoid arthritis study

REACH study 
Geuskens et al, 2008 and Alves et al, 2011

> Geuskens GA, Hazes JMW, Barendregt PJ, Burdorf A. Work and sick leave among patients with early inflammatory joint conditions. Arthritis Rheum. 2008;59: 1458–1466. doi:10.1002/art.24104
> Alves C, Luime JJ, van Zeben D, Huisman A-M, Weel AEAM, Barendregt PJ, et al. Diagnostic performance of the ACR/EULAR 2010 criteria for rheumatoid arthritis and two diagnostic algorithms in an early arthritis clinic (REACH). Ann Rheum Dis. 2011;70: 1645–1647. doi:10.1136/ard.2010.142299

### Examples

- Example XI.4: Bayesian variable selection (BVS) based on the BIC approximation p. 330
- Example XI.6: BVS based on a generalized Zellner's $g$-prior p. 335
- Example XI.7: BVS using RJMCMC p. 338
- Example XI.8: BVS using stochastic search variable selection (SSVS) p. 342
- Example XI.12: BVS and choosing the appropriate scale of the covariates


### Data files
```
├── reach.txt
├── reach.csv
```

### Variables

- accp (cyclic citrullinated peptide antibody), 
- age, 
- esr (erythrocyte sedimentation rate), 
- dc (duration of complaints in days), 
- stiffness (duration of morning stiffness in minutes), 
- rf (rheumatoid factor), 
- gender, 
- sym (symmetrical pattern of joint inflammation yes/no), 
- sjc (swollen joint count), 
- tjc (tender joint count), 
- bcph (bilateral compression pain in hands yes/no) and 
- bcpf (bilateral compression pain in feet yes/no)



# Book contents overview

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

# Book detailed contents

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