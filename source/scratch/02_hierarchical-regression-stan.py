# ---
# jupyter:
#   celltoolbar: Slideshow
#   jupytext:
#     cell_metadata_json: true
#     formats: ipynb,md,py:percent
#     notebook_metadata_filter: all
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.14.0
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
#   language_info:
#     codemirror_mode:
#       name: ipython
#       version: 3
#     file_extension: .py
#     mimetype: text/x-python
#     name: python
#     nbconvert_exporter: python
#     pygments_lexer: ipython3
#     version: 3.10.5
#   name: Betancourt's Probabilistic Modelling Workflow in numpyro
#   rise:
#     scroll: true
#     theme: black
#   toc-autonumbering: true
#   toc-showcode: false
#   toc-showmarkdowntxt: false
#   toc-showtags: false
# ---

# %% [markdown] {"slideshow": {"slide_type": "slide"}}
# # Hierarchical regression

# %% [markdown] {"slideshow": {"slide_type": "fragment"}}
# The following notes are based on 
# * <cite data-cite="Gelman1999-yu">Gelman, Krantz, Lin, and Price (1999)</cite>
# * [Chris Fonnesbeck - Stan Workshop 2016 - Multilevel Modeling](https://github.com/fonnesbeck/stan_workshop_2016/blob/master/notebooks/Multilevel%20Modeling.ipynb)
# * <cite data-cite="Gelman2006-uo">Gelman and Hill (2006)</cite>

# %% [markdown] {"heading_collapsed": "true", "slideshow": {"slide_type": "slide"}, "tags": []}
# ## Setup

# %% [markdown] {"tags": []}
# ### Install libraries

# %% {"slideshow": {"slide_type": "fragment"}, "tags": []}
# # %run -i 'plotting.py'

# %%
# # !apt-get install -y fonts-lmodern
# # !pip install -q arviz numpyro

# %% [markdown] {"tags": []}
# ### Add latin modern fonts

# %%
import matplotlib.pyplot as plt
import matplotlib.font_manager

# %%
## fonts_path = "/usr/share/texmf/fonts/opentype/public/lm/" #ubuntu
## fonts_path = "~/Library/Fonts/" # macos
fonts_path = "/usr/share/fonts/OTF/" # arch
matplotlib.font_manager.fontManager.addfont(fonts_path + "lmsans10-regular.otf")
matplotlib.font_manager.fontManager.addfont(fonts_path + "lmroman10-regular.otf")

# %% [markdown]
# ### Set matplotlib to use latin modern fonts

# %% {"tags": []}
from IPython.display import set_matplotlib_formats
# from IPython import matplotlib_inline
# ##%matplotlib inline
set_matplotlib_formats('svg') # use SVG backend to maintain vectorization
# matplotlib_inline.backend_inline.set_matplotlib_formats('svg')  # use SVG backend to maintain vectorization
plt.style.use('default') #reset default parameters
## https://stackoverflow.com/a/3900167/446907
plt.rcParams.update({'font.size': 16,
                     'font.family': ['sans-serif'],
                     'font.serif': ['Latin Modern Roman'] + plt.rcParams['font.serif'],
                     'font.sans-serif': ['Latin Modern Sans'] + plt.rcParams['font.sans-serif']})

# %% [markdown] {"slideshow": {"slide_type": "slide"}, "tags": [], "jp-MarkdownHeadingCollapsed": true}
# ## Generative models

# %% [markdown] {"slideshow": {"slide_type": "subslide"}}
# ### Example generative models

# %% [markdown] {"slideshow": {"slide_type": "subslide"}}
# #### Univariate normal model

# %% [markdown] {"slideshow": {"slide_type": "fragment"}}
# From a very simple perspective, generative modeling refers to the situation in which we develop a candidate probabilistic specification of the process from which our data are generated. Usually this will include the specification of prior distributions over all first-order parameters.

# %% [markdown] {"slideshow": {"slide_type": "fragment"}}
# <div>
# <center>    
# <img src="https://www.bayespy.org/_images/tikz-57bc0c88a2974f4c1e2335fe9edb88ff2efdf970.png" style="background-color:white;" alt="Drawing" width="10%"/></center>
# </div>

# %% [markdown] {"slideshow": {"slide_type": "fragment"}}
# \begin{equation*}
# \begin{split}
# p(\mathbf{y}|\mu,\tau) &= \prod^{9}_{n=0} \mathcal{N}(y_n|\mu,\tau) \\
# p(\mu) &= \mathcal{N}(\mu|0,10^{-6}) \\
# p(\tau) &= \mathcal{G}(\tau|10^{-6},10^{-6})
# \end{split}
# \end{equation*}

# %% [markdown] {"slideshow": {"slide_type": "fragment"}}
# This comes from the library [bayespy](https://github.com/bayespy/bayespy/blob/develop/doc/source/user_guide/quickstart.rst). The best description we are aware of regarding the syntax and semantics of graphical models via factor graph notation is in the [tikz-bayesnet](https://github.com/jluttine/tikz-bayesnet) library [technical report](https://github.com/jluttine/tikz-bayesnet/blob/master/dietz-techreport.pdf).

# %% [markdown] {"slideshow": {"slide_type": "subslide"}}
# #### Multivariate normal models

# %% [markdown] {"slideshow": {"slide_type": "fragment"}}
# <div>
# <center>    
# <img src="https://www.bayespy.org/_images/tikz-80a1db369be1f25b61ceacfff551dae2bdd331c3.png" style="background-color:white;" alt="Drawing" width="10%"/></center>
# </div>

# %% [markdown] {"slideshow": {"slide_type": "fragment"}}
# $$\mathbf{y}_{mn} \sim \mathcal{N}(\boldsymbol{\mu}, \mathbf{\Lambda}),\qquad m=0,\ldots,9, \quad n=0,\ldots,29.$$

# %% [markdown] {"slideshow": {"slide_type": "subslide"}}
# <div>
# <center>    
# <img src="https://www.bayespy.org/_images/tikz-97236981a2be663d10ade1ad85caa727621615db.png" style="background-color:white;" alt="Drawing" width="20%"/></center>
# </div>

# %% [markdown] {"slideshow": {"slide_type": "fragment"}}
# $$\mathbf{y}_{mn} \sim \mathcal{N}(\boldsymbol{\mu}_m,
# \mathbf{\Lambda}_n),\qquad m=0,\ldots,9, \quad n=0,\ldots,29.$$
#
# Note that these are for illustrative purposes of the manner in which our data can share parameters and we have not yet defined priors over our parameters.

# %% [markdown] {"slideshow": {"slide_type": "slide"}, "tags": []}
# ## Example of linear regression

# %% [markdown] {"tags": []}
# ### Setup

# %% [markdown] {"tags": []}
# #### Load libraries

# %% {"slideshow": {"slide_type": "fragment"}, "tags": []}
# ## %pylab inline
import matplotlib.pyplot as plt
import pandas as pd
import scipy.stats as stats
import seaborn as sns
import numpy as np
## plt.style.use(['seaborn-talk'])
## plt.rcParams["figure.figsize"] = (10,8)

import arviz as az
import jax
import jax.numpy as jnp
import numpyro
import numpyro.distributions as dist
from numpyro.infer import MCMC, NUTS, Predictive
print(numpyro.__version__)
print(jax.__version__)
print(az.__version__)

numpyro.set_platform("cpu")
numpyro.set_host_device_count(4)

# %% [markdown] {"slideshow": {"slide_type": "fragment"}, "jp-MarkdownHeadingCollapsed": true, "tags": []}
# #### define colors

# %% {"slideshow": {"slide_type": "fragment"}, "tags": []}
c_light ="#DCBCBC"
c_light_highlight ="#C79999"
c_mid ="#B97C7C"
c_mid_highlight ="#A25050"
c_dark ="#8F2727"
c_dark_highlight ="#7C0000"

# %% [markdown]
# ### Import data

# %% [markdown]
# Import radon data

# %%
srrs2 = pd.read_csv('http://www.stat.columbia.edu/~gelman/arm/examples/radon/srrs2.dat')
srrs2.columns = srrs2.columns.map(str.strip)
srrs_mn = srrs2.assign(fips=srrs2.stfips*1000 + srrs2.cntyfips)[srrs2.state=='MN']

# %% {"tags": []}
print(type(srrs_mn))
srrs_mn.shape

# %% {"tags": []}
srrs_mn.iloc[list(range(1,7))+list(range(800,806)),:]

# %%
sorted(srrs_mn)

# %%
list(srrs_mn.columns)

# %%
cty = pd.read_csv('http://www.stat.columbia.edu/~gelman/arm/examples/radon/cty.dat')
cty_mn = cty[cty.st=='MN'].copy()
cty_mn[ 'fips'] = 1000*cty_mn.stfips + cty_mn.ctfips

# %% {"tags": []}
print(cty_mn.shape)
type(cty_mn)

# %% {"tags": []}
cty_mn.iloc[list(range(1,7))+list(range(80,86)),:]

# %% {"tags": []}
sorted(cty_mn)

# %% [markdown]
# ### Transform data

# %% [markdown]
# Combine the home and county data.

# %%
srrs_mn = srrs_mn.merge(cty_mn[['fips', 'Uppm']], on='fips')
srrs_mn = srrs_mn.drop_duplicates(subset='idnum')

# %%
n = len(srrs_mn)

# %%
u = np.log(srrs_mn.Uppm)

# %%
list(srrs_mn.columns)

# %%
srrs_mn.apply(lambda x: pd.Series([x.min(), x.max()])).T.values.tolist()

# %% {"tags": []}
pd.set_option("max_columns", None)
srrs_mn.describe().loc[['min','max']]
# pd.reset_option("max_columns")

# %%
sorted(srrs_mn)

# %%
srrs_mn.head()

# %%
srrs_mn.shape

# %% [markdown]
# Create a list of the counties in Minnesota.

# %%
srrs_mn.county = srrs_mn.county.str.strip()
mn_counties = srrs_mn.county.unique()
counties = len(mn_counties)

# %% {"tags": []}
print(mn_counties.shape)
mn_counties[0:5]

# %% [markdown]
# Extract relevant variables

# %%
county_lookup = dict(zip(mn_counties, range(len(mn_counties))))
county = srrs_mn['county_code'] = srrs_mn.county.replace(county_lookup).values
radon = srrs_mn.activity
srrs_mn['log_radon'] = log_radon = np.log(radon + 0.1).values
floor_measure = srrs_mn.floor.values

# %% [markdown]
# Distribution of logarithmic radon levels across the entire state of Minnesota.

# %%
srrs_mn.activity.apply(lambda x: np.log(x+0.1)).hist(bins=25)

# %% [markdown] {"tags": []}
# ### Complete pooling model

# %% {"tags": []}
# import stan
from cmdstanpy import cmdstan_path, CmdStanModel
import os
import json

# %% [markdown]
# The complete pooling model considers houses within all counties to be the same. As such there is only one set of parameters required in this model.
#
# $$ y_i = \alpha + \beta x_i + \epsilon_i $$
#
# which may be written
#
# $$ y_i \sim \mathcal{N} (\alpha + \beta x_i, \sigma) $$

# %% [markdown]
# We define the data for this model, which includes the number of samples ($N$), floor-within-house predictors ($x$), and the outcomes of log-radon measurments ($y$).

# %%
pooled_data = """
data{
    int<lower=0> N;
    vector[N] x;
    vector[N] y;
}
"""

# %% [markdown]
# We define initializations for the parameters $\alpha$ and $\beta$.

# %%
pooled_parameters = """
parameters {
    vector[2] beta;
    real<lower=0> sigma;
}
"""

# %% [markdown]
# Model the log-radon measurements as samples from a normal distribution with mean a function of the floor of measurement.

# %%
pooled_model = """
model {
    y ~ normal(beta[1] + beta[2] * x, sigma);
}
"""

# %% {"tags": []}
pooled_model_file = open("pooled_model.stan", "w")
pooled_model_file.write(pooled_data + pooled_parameters + pooled_model)
pooled_model_file.close()

# %% [markdown]
# Recall the range of values for the floor predictor, $x$ is binary (ground vs other floor).

# %% {"tags": []}
srrs_mn.floor.unique()
np.unique(floor_measure)

# %% {"tags": []}
pooled_data_dict = {'N': len(log_radon),
               'x': floor_measure.tolist(),
               'y': log_radon.tolist()}

# %% {"tags": []}
pooled_data_file = open("pooled_model.data.json", "w")
json.dump(pooled_data_dict, pooled_data_file)
pooled_data_file.close()

# %% {"tags": []}
pooled_stan = os.path.join('pooled_model.stan')

# %% {"tags": []}
pooled_stan_model = CmdStanModel(stan_file=pooled_stan)

# %%
pooled_stan_data = os.path.join('pooled_model.data.json')

# %%
pooled_stan_fit = pooled_stan_model.sample(chains=2, iter_sampling=1000 , data=pooled_stan_data)

# %% {"tags": []}
az.plot_density(pooled_stan_fit, var_names=["beta", "sigma"])

# %% {"tags": []}
pooled_model_summary = pooled_stan_fit.summary(percentiles=[20,40,60,80])
pooled_model_summary

# %% {"tags": []}
plt.scatter(srrs_mn.floor, np.log(srrs_mn.activity+0.1))
xvals = np.linspace(-0.2, 1.2)
plt.plot(xvals, pooled_model_summary['Mean']['beta[2]']*xvals+pooled_model_summary['Mean']['beta[1]'], 'r--')

# %% [markdown] {"tags": []}
# ### No pooling model

# %% [markdown]
# The no pooling model considers houses in each county to be independent from one another. There are as many pairs of parameters as there are counties in this model.
# $$ y_i = \alpha_{j[i]} + \beta x_i + \epsilon_i $$
# which may also be written
#
# $$ y_i \sim \mathcal{N} (\alpha_{j[i]} + \beta x_i, \sigma) $$

# %%
unpooled_model = """data {
  int<lower=0> N; 
  int<lower=1,upper=85> county[N];
  vector[N] x;
  vector[N] y;
} 
parameters {
  vector[85] a;
  real beta;
  real<lower=0,upper=100> sigma;
} 
transformed parameters {
  vector[N] y_hat;

  for (i in 1:N)
    y_hat[i] <- beta * x[i] + a[county[i]];
}
model {
  y ~ normal(y_hat, sigma);
}"""

# %% {"tags": []}
unpooled_model_file = open("unpooled_model.stan", "w")
unpooled_model_file.write(unpooled_model)
unpooled_model_file.close()

# %% {"tags": []}
print(county.shape)
np.unique(county)

# %% {"tags": []}
unpooled_data_dict = {'N': len(log_radon),
               'county': (county+1).tolist(), # Stan counts starting at 1
               'x': floor_measure.tolist(),
               'y': log_radon.tolist()}

# %% {"tags": []}
unpooled_data_file = open("unpooled_model.data.json", "w")
json.dump(unpooled_data_dict, unpooled_data_file)
unpooled_data_file.close()

# %%
unpooled_stan = os.path.join('unpooled_model.stan')
unpooled_stan_model = CmdStanModel(stan_file=unpooled_stan)

# %% {"tags": []}
unpooled_stan_data = os.path.join('unpooled_model.data.json')
unpooled_stan_fit = unpooled_stan_model.sample(chains=2, iter_sampling=1000 , sig_figs=6, data=unpooled_stan_data)

# %% {"tags": []}
unpooled_stan_fit.save_csvfiles(dir='stan/')

# %% {"tags": []}
az.plot_density(unpooled_stan_fit, var_names=["beta", "sigma"])

# %% {"tags": []}
unpooled_model_summary = unpooled_stan_fit.summary(percentiles=[20,40,60,80], sig_figs=4)
unpooled_model_summary

# %% {"tags": []}
unpooled_stan_fit.diagnose();

# %% {"tags": []}
unpooled_model_intercepts = unpooled_model_summary.filter(regex='^a.*', axis=0)
unpooled_model_intercepts

# %% {"tags": []}
unpooled_model_intercepts["County"] = [*range(1,len(unpooled_model_intercepts)+1)]
unpooled_model_intercepts["County Name"] = mn_counties
unpooled_model_intercepts_sorted = unpooled_model_intercepts.sort_values("Mean", axis=0)
unpooled_model_intercepts_sorted["Order"] = [*range(1,len(unpooled_model_intercepts)+1)]
unpooled_model_intercepts_sorted

# %% {"tags": []}
ax = unpooled_model_intercepts_sorted.plot.scatter(x="Order", y="Mean", c="County", 
                                                   colormap=plt.cm.get_cmap('Set2', 8))
ax.errorbar(unpooled_model_intercepts_sorted["Order"], unpooled_model_intercepts_sorted["Mean"], 
            yerr=unpooled_model_intercepts_sorted["StdDev"], xerr=None, color="black", alpha=0.5, capsize=0.2, linewidth=0.2, ls='none')
ax.set_xlabel("Ordered county")
ax.set_ylabel("Radon estimate $(\log_{10})$")

# %% {"tags": []}
sample_counties = ('LAC QUI PARLE', 'AITKIN', 'KOOCHICHING', 
                    'DOUGLAS', 'CLAY', 'STEARNS', 'RAMSEY', 'ST LOUIS')

fig, axes = plt.subplots(2, 4, figsize=(12, 6), sharey=True, sharex=True)
axes = axes.ravel()
m = unpooled_model_summary["Mean"]["beta"]
m0 = pooled_model_summary['Mean']['beta[2]']
b0 = pooled_model_summary['Mean']['beta[1]']

for i,c in enumerate(sample_counties):
    y = srrs_mn.log_radon[srrs_mn.county==c]
    x = srrs_mn.floor[srrs_mn.county==c]
    axes[i].scatter(x + np.random.randn(len(x))*0.01, y, alpha=0.4)
    
    # No pooling model
    b = unpooled_model_intercepts[unpooled_model_intercepts["County Name"]==c]["Mean"].values[0]
    
    # Plot both models and data
    xvals = np.linspace(-0.2, 1.2)
    axes[i].plot(xvals, m*xvals+b)
    axes[i].plot(xvals, m0*xvals+b0, 'r--')
    axes[i].set_xticks([0,1])
    axes[i].set_xticklabels(['basement', 'floor'])
    axes[i].set_ylim(-1, 3)
    axes[i].set_title(c)
    if not i%4:
        axes[i].set_ylabel('log radon level')

# %%
