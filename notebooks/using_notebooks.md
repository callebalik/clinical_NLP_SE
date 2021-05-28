Notebooks are for exploration and communication

Subdivide the notebooks folder. For example, notebooks/exploratory contains initial explorations, whereas notebooks/reports is more polished work that can be exported as html to the reports directory.

notebooks are challenging objects for source control (e.g., diffs of the json are often not human-readable and merging is near impossible) --> don't collaborate directly with others on Jupyter notebooks. There are two steps we recommend for using notebooks effectively:

    Follow a naming convention that shows the owner and the order the analysis was done in. We use the format <step>-<ghuser>-<description>.ipynb (e.g., 0.3-bull-visualize-distributions.ipynb).

    Refactor the good parts. Don't write code to do the same task in multiple notebooks. If it's a data preprocessing task, put it in the pipeline at src/data/make_dataset.py and load data from data/interim. If it's useful utility code, refactor it to src.

Now by default we turn the project into a Python package (see the setup.py file). You can import your code and use it in notebooks with a cell like the following:

```
# OPTIONAL: Load the "autoreload" extension so that code can change
%load_ext autoreload

# OPTIONAL: always reload modules so that as you change code in src, it gets loaded
%autoreload 2

from src.data import make_dataset
```