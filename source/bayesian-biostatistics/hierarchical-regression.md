---
jupyter:
  celltoolbar: Slideshow
  jupytext:
    cell_metadata_json: true
    formats: ipynb,md,py:percent
    notebook_metadata_filter: all
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.3'
      jupytext_version: 1.11.2
  kernelspec:
    display_name: Python 3
    language: python
    name: python3
  language_info:
    codemirror_mode:
      name: ipython
      version: 3
    file_extension: .py
    mimetype: text/x-python
    name: python
    nbconvert_exporter: python
    pygments_lexer: ipython3
    version: 3.9.5
  name: Betancourt's Probabilistic Modelling Workflow in numpyro
  rise:
    scroll: true
    theme: black
  toc-autonumbering: true
  toc-showcode: false
  toc-showmarkdowntxt: false
  toc-showtags: false
---

<!-- #region {"slideshow": {"slide_type": "slide"}} -->
# Hierarchical regression
<!-- #endregion -->

<!-- #region {"slideshow": {"slide_type": "fragment"}} -->
The following notes are based on <cite data-cite="Gelman2006-uo">Gelman and Hill (2006)</cite>.
<!-- #endregion -->

<!-- #region {"heading_collapsed": "true", "slideshow": {"slide_type": "slide"}, "tags": []} -->
## Setup
<!-- #endregion -->

### Install libraries

```python slideshow={"slide_type": "fragment"} tags=[]
# %run -i 'plotting.py'
```

```python
# !apt-get install -y fonts-lmodern
# !pip install -q arviz numpyro
```

### Add latin modern fonts

```python
import matplotlib.pyplot as plt
import matplotlib.font_manager
```

```python
## fonts_path = "/usr/share/texmf/fonts/opentype/public/lm/" #ubuntu
## fonts_path = "~/Library/Fonts/" # macos
fonts_path = "/usr/share/fonts/OTF/" # arch
matplotlib.font_manager.fontManager.addfont(fonts_path + "lmsans10-regular.otf")
matplotlib.font_manager.fontManager.addfont(fonts_path + "lmroman10-regular.otf")
```

### Set matplotlib to use latin modern fonts

```python
from IPython.display import set_matplotlib_formats
##%matplotlib inline
set_matplotlib_formats('svg') # use SVG backend to maintain vectorization
plt.style.use('default') #reset default parameters
## https://stackoverflow.com/a/3900167/446907
plt.rcParams.update({'font.size': 16,
                     'font.family': ['sans-serif'],
                     'font.serif': ['Latin Modern Roman'] + plt.rcParams['font.serif'],
                     'font.sans-serif': ['Latin Modern Sans'] + plt.rcParams['font.sans-serif']})
```

<!-- #region {"slideshow": {"slide_type": "slide"}} -->
## Generative models
<!-- #endregion -->

<!-- #region {"slideshow": {"slide_type": "subslide"}} -->
### Example generative models
<!-- #endregion -->

<!-- #region {"slideshow": {"slide_type": "subslide"}} -->
#### Univariate normal model
<!-- #endregion -->

<!-- #region {"slideshow": {"slide_type": "fragment"}} -->
From a very simple perspective, generative modeling refers to the situation in which we develop a candidate probabilistic specification of the process from which our data are generated. Usually this will include the specification of prior distributions over all first-order parameters.
<!-- #endregion -->

<!-- #region {"slideshow": {"slide_type": "fragment"}} -->
<div>
<center>    
<img src="https://www.bayespy.org/_images/tikz-57bc0c88a2974f4c1e2335fe9edb88ff2efdf970.png" style="background-color:white;" alt="Drawing" width="10%"/></center>
</div>
<!-- #endregion -->

<!-- #region {"slideshow": {"slide_type": "fragment"}} -->
\begin{equation*}
\begin{split}
p(\mathbf{y}|\mu,\tau) &= \prod^{9}_{n=0} \mathcal{N}(y_n|\mu,\tau) \\
p(\mu) &= \mathcal{N}(\mu|0,10^{-6}) \\
p(\tau) &= \mathcal{G}(\tau|10^{-6},10^{-6})
\end{split}
\end{equation*}
<!-- #endregion -->

<!-- #region {"slideshow": {"slide_type": "fragment"}} -->
This comes from the library [bayespy](https://github.com/bayespy/bayespy/blob/develop/doc/source/user_guide/quickstart.rst). The best description we are aware of regarding the syntax and semantics of graphical models via factor graph notation is in the [tikz-bayesnet](https://github.com/jluttine/tikz-bayesnet) library [technical report](https://github.com/jluttine/tikz-bayesnet/blob/master/dietz-techreport.pdf).
<!-- #endregion -->

<!-- #region {"slideshow": {"slide_type": "subslide"}} -->
#### Multivariate normal models
<!-- #endregion -->

<!-- #region {"slideshow": {"slide_type": "fragment"}} -->
<div>
<center>    
<img src="https://www.bayespy.org/_images/tikz-80a1db369be1f25b61ceacfff551dae2bdd331c3.png" style="background-color:white;" alt="Drawing" width="10%"/></center>
</div>
<!-- #endregion -->

<!-- #region {"slideshow": {"slide_type": "fragment"}} -->
$$\mathbf{y}_{mn} \sim \mathcal{N}(\boldsymbol{\mu}, \mathbf{\Lambda}),\qquad m=0,\ldots,9, \quad n=0,\ldots,29.$$
<!-- #endregion -->

<!-- #region {"slideshow": {"slide_type": "subslide"}} -->
<div>
<center>    
<img src="https://www.bayespy.org/_images/tikz-97236981a2be663d10ade1ad85caa727621615db.png" style="background-color:white;" alt="Drawing" width="20%"/></center>
</div>
<!-- #endregion -->

<!-- #region {"slideshow": {"slide_type": "fragment"}} -->
$$\mathbf{y}_{mn} \sim \mathcal{N}(\boldsymbol{\mu}_m,
\mathbf{\Lambda}_n),\qquad m=0,\ldots,9, \quad n=0,\ldots,29.$$

Note that these are for illustrative purposes of the manner in which our data can share parameters and we have not yet defined priors over our parameters.
<!-- #endregion -->

<!-- #region {"slideshow": {"slide_type": "slide"}} -->
## Example of linear regression
<!-- #endregion -->

### Setup


#### Load libraries

```python slideshow={"slide_type": "fragment"}
## %pylab inline
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
```

<!-- #region {"slideshow": {"slide_type": "fragment"}} -->
#### define colors
<!-- #endregion -->

```python slideshow={"slide_type": "fragment"}
c_light ="#DCBCBC"
c_light_highlight ="#C79999"
c_mid ="#B97C7C"
c_mid_highlight ="#A25050"
c_dark ="#8F2727"
c_dark_highlight ="#7C0000"
```
