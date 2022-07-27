---
jupyter:
  celltoolbar: Slideshow
  jupytext:
    cell_metadata_json: true
    formats: ipynb,md
    notebook_metadata_filter: celltoolbar,rise,toc-autonumbering,toc-showcode,toc-showmarkdowntxt
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.3'
      jupytext_version: 1.11.2
  kernelspec:
    display_name: Julia 1.6.1
    language: julia
    name: julia-1.6
  rise:
    scroll: true
    theme: black
  toc-autonumbering: true
  toc-showcode: false
  toc-showmarkdowntxt: false
---

<!-- #region {"tags": []} -->
# Classical regression in Turing
<!-- #endregion -->

<!-- #region {"tags": []} -->
## Setup plotting
<!-- #endregion -->

```julia tags=[]
using PyCall
font_manager = pyimport("matplotlib.font_manager")
font_manager.fontManager.addfont("/usr/share/fonts/OTF/lmroman10-regular.otf")
PyDict(pyimport("matplotlib")["rcParams"])["font.serif"] = ["Latin Modern Roman"]
# font_manager.fontManager.addfont("/usr/share/fonts/OTF/lmsans10-regular.otf")
# PyDict(pyimport("matplotlib")["rcParams"])["font.serif"] = ["Latin Modern Sans"]
```

```julia tags=[]
using Plots
font = Plots.font("Latin Modern Roman", 18)
# font = Plots.font("Latin Modern Sans", 18)
pyplot(titlefont=font, guidefont=font, xtickfont=font, ytickfont=font, legendfont=font)
```

```julia tags=[]
x = 1:10; y = rand(10); # These are the plotting data
plot(x, y)
```

<!-- #region {"tags": []} -->
## Import libraries
<!-- #endregion -->

<!-- #region {"tags": []} -->
You may need to install `julia` package `ForwardDiff` if it isn't already installed.
```bash
julia -e 'using Pkg; Pkg.status()'
julia -e 'using Pkg; Pkg.instantiate(); Pkg.API.precompile()'
julia -e 'using Pkg; Pkg.add("ForwardDiff")'
```
<!-- #endregion -->

```julia tags=[]
# Import Turing and Distributions.
using Turing, Distributions

# Import RDatasets.
using RDatasets

# Import MCMCChains, Plots, and StatPlots for visualizations and diagnostics.
using MCMCChains, Plots, StatsPlots

# Functionality for splitting and normalizing the data.
using MLDataUtils: shuffleobs, splitobs, rescale!

# Functionality for evaluating the model predictions.
using Distances

# Functionality for reading CSV files into DataFrames
using CSV
using DataFrames

# Set a seed for reproducibility.
using Random
Random.seed!(0)

# Hide the progress prompt while sampling.
# Turing.turnprogress(false);
```

<!-- #region {"tags": []} -->
## Load data
<!-- #endregion -->

```julia tags=[]
# Import the "Default" dataset.
data = RDatasets.dataset("datasets", "mtcars");

# Show the first six rows of the dataset.
print(size(data))
first(data, 6)
```

<!-- #region {"tags": []} -->
## Preprocess data
<!-- #endregion -->

<!-- #region {"tags": []} -->
### Manipulate data structure into appropriate input form
<!-- #endregion -->

Extract a training and testing set from the data

```julia
# Remove the model column.
select!(data, Not(:Model))

# Split our dataset 70%/30% into training/test sets.
trainset, testset = splitobs(shuffleobs(data), 0.7)
```

Specify the outcome variable for predicton.

```julia
target = :MPG
```

Convert data to matrix form.

```julia
train = Matrix(select(trainset, Not(target)))
```

```julia
test = Matrix(select(testset, Not(target)))
```

```julia tags=[]
train_target = trainset[:, target];
test_target = testset[:, target];
```

<!-- #region {"tags": []} -->
### Transform data
<!-- #endregion -->

Standardize the data features.

```julia
μ, σ = rescale!(train; obsdim = 1)
```

```julia
train
```

```julia
rescale!(test, μ, σ; obsdim = 1)
```

```julia
test
```

Standardize outcome data as well.

```julia
μtarget, σtarget = rescale!(train_target; obsdim = 1);
rescale!(test_target, μtarget, σtarget; obsdim = 1);
```

<!-- #region {"tags": []} -->
## Define model
<!-- #endregion -->

One linear model to predict the outcome variable `MPG` from the other variables in the data set is a so-called fixed effects model given by

$$
\mathrm{MPG}_i \sim \mathcal{N}(\alpha + \beta^T \mathbf{X}_i, \sigma^2)
$$

Note here that the slope parameters $\beta^T$ and the intercept $\alpha$ are fixed across all data.

```julia

```
