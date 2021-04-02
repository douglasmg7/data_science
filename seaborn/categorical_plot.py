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

#  sns.barplot(x='sex', y='total_bill', data=tips)

#  import numpy as np
#  sns.barplot(x='sex', y='total_bill', data=tips, estimator=np.std)

#  sns.countplot(x='sex', data=tips)

#  sns.boxplot(x='day', y='total_bill', data=tips)
#  sns.boxplot(x='day', y='total_bill', data=tips, hue='smoker')

#  sns.violinplot(x='day', y='total_bill', data=tips)
#  sns.violinplot(x='day', y='total_bill', data=tips, hue='sex')
#  sns.violinplot(x='day', y='total_bill', data=tips, hue='sex', split=True)

#  sns.stripplot(x='day', y='total_bill', data=tips)
#  sns.stripplot(x='day', y='total_bill', data=tips, jitter=False)
#  sns.stripplot(x='day', y='total_bill', data=tips, hue='sex', split=True)

#  sns.swarmplot(x='day', y='total_bill', data=tips)

# Join two types of plot
#  sns.violinplot(x='day', y='total_bill', data=tips)
#  sns.swarmplot(x='day', y='total_bill', data=tips, color='black')

# factorplot changed to catplot
#  sns.catplot(x='day', y='total_bill', data=tips, kind='bar')
sns.catplot(x='day', y='total_bill', data=tips, kind='violin')



plt.show()
