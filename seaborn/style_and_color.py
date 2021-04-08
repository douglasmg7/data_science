#!/usr/bin/env python3

import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset('tips')
#  print(tips.head())
#  print(tips.info())

   #  total_bill   tip     sex smoker  day    time  size
#  0       16.99  1.01  Female     No  Sun  Dinner     2
#  1       10.34  1.66    Male     No  Sun  Dinner     3
#  2       21.01  3.50    Male     No  Sun  Dinner     3
#  3       23.68  3.31    Male     No  Sun  Dinner     2
#  4       24.59  3.61  Female     No  Sun  Dinner     4

#  #  sns.set_style('white')
#  #  sns.set_style('ticks')   # not working
#  #  sns.set_style('darkgrid')
#  #  plt.figure(figsize=(32,3))   # not working
#  #  sns.set_style('whitegrid')
#  sns.countplot(x='sex', data=tips)
#  sns.despine()

#  #  sns.set_context('notebook')
#  sns.set_context('poster', font_scale=.8)
#  sns.countplot(x='sex', data=tips)

sns.lmplot(x='total_bill', y='tip', data=tips, hue='sex')

plt.show()
