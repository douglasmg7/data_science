#!/usr/bin/env python3

# A kernel density estimate (KDE) plot is a method for visualizing the distribution of observations in a dataset, analagous to a histogram.
# KDE represents the data using a continuous probability density curve in one or more dimensions

import seaborn as sns
import matplotlib.pyplot as plt

# example data
tips = sns.load_dataset('tips')
flgihts = sns.load_dataset('flights')

#  print(flgihts.head())
#  print(flgihts.info())

   #  total_bill   tip     sex smoker  day    time  size
#  0       16.99  1.01  Female     No  Sun  Dinner     2
#  1       10.34  1.66    Male     No  Sun  Dinner     3
#  2       21.01  3.50    Male     No  Sun  Dinner     3
#  3       23.68  3.31    Male     No  Sun  Dinner     2
#  4       24.59  3.61  Female     No  Sun  Dinner     4

   #  year month  passengers
#  0  1949   Jan         112
#  1  1949   Feb         118
#  2  1949   Mar         132
#  3  1949   Apr         129
#  4  1949   May         121

#  # make it a matix
#  tc = tips.corr()
#  #  print(tc)
#  #  sns.heatmap(tc)
#  sns.heatmap(tc, annot=True, cmap='coolwarm')

#  print(flgihts.pivot_table(index='month', columns='year', values='passengers'))

#  fp = flgihts.pivot_table(index='month', columns='year', values='passengers')
#  sns.heatmap(fp, cmap='coolwarm', linecolor='white', linewidth=3)

#  fp = flgihts.pivot_table(index='month', columns='year', values='passengers')
fp = flgihts.pivot_table(index='month', columns='year', values='passengers')
sns.clustermap(fp, cmap='coolwarm', standard_scale=1)


plt.show()
