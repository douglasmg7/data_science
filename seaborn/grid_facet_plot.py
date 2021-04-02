#!/usr/bin/env python

import matplotlib.pyplot as plt
import seaborn as sns


tips = sns.load_dataset('tips')
print(tips.info())

g = sns.FacetGrid(data=tips, col='time', row='smoker')
#  g.map(sns.histplot, 'total_bill')

g.map(plt.scatter, 'total_bill', 'tip')

plt.show()