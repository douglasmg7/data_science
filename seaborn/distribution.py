#!/usr/bin/env python3

# A kernel density estimate (KDE) plot is a method for visualizing the distribution of observations in a dataset, analagous to a histogram.
# KDE represents the data using a continuous probability density curve in one or more dimensions

import seaborn as sns
import matplotlib.pyplot as plt

# example data
tips = sns.load_dataset('tips')
#  print(tips.head())
#  print(tips.info())

   #  total_bill   tip     sex smoker  day    time  size
#  0       16.99  1.01  Female     No  Sun  Dinner     2
#  1       10.34  1.66    Male     No  Sun  Dinner     3
#  2       21.01  3.50    Male     No  Sun  Dinner     3
#  3       23.68  3.31    Male     No  Sun  Dinner     2
#  4       24.59  3.61  Female     No  Sun  Dinner     4

# hist
#  sns.distplot(tips['total_bill'], kde=False)
#  sns.histplot(tips['total_bill'], kde=False, bins=40)

sns.kdeplot(tips['total_bill'])

# join, two paramas relationship
#  sns.jointplot(x='total_bill', y='tip', data=tips)
#  sns.jointplot(x='total_bill', y='tip', data=tips, kind='hex')
#  sns.jointplot(x='total_bill', y='tip', data=tips, kind='reg')
#  sns.jointplot(x='total_bill', y='tip', data=tips, kind='kde')

# like a join for all fields
#  sns.pairplot(tips)
#  sns.pairplot(tips, hue='sex')   # color poinst by sex

# like a hist
#  sns.rugplot(tips['total_bill'])




plt.show()
