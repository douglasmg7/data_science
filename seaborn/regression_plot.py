#!/usr/bin/env python

import matplotlib.pyplot as plt
import seaborn as sns


tips = sns.load_dataset('tips')
#  print(tips.head())
#  print(tips.info())

#  sns.lmplot(x='total_bill', y='tip', data=tips)
#  sns.lmplot(x='total_bill', y='tip', data=tips, hue='sex', markers=['o', 'v'], scatter_kws={'s': 50})
#  sns.lmplot(x='total_bill', y='tip', data=tips, col='sex')
#  sns.lmplot(x='total_bill', y='tip', data=tips, col='sex', row='time')
#  sns.lmplot(x='total_bill', y='tip', data=tips, col='day', row='time', hue='sex')
sns.lmplot(x='total_bill', y='tip', data=tips, col='day', hue='sex', aspect=.6, size=8)

plt.show()