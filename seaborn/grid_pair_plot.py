#!/usr/bin/env python

import matplotlib.pyplot as plt
import seaborn as sns


iris = sns.load_dataset('iris')
#  print(iris.head())
#  print(iris.info())
#  print(iris['species'].unique())

# create sub plots
g = sns.PairGrid(iris)
#  g.map(plt.scatter)
g.map_diag(sns.histplot)
g.map_upper(plt.scatter)
g.map_lower(sns.kdeplot)

plt.show()