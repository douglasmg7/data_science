#!/usr/bin/env python

import numpy as np
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('df3',)

#  print(df.head())
          #  a         b         c         d
#  0  0.336272  0.325011  0.001020  0.401402
#  1  0.980265  0.831835  0.772288  0.076485
#  2  0.480387  0.686839  0.000575  0.746758
#  3  0.502106  0.305142  0.768608  0.654685
#  4  0.856602  0.171448  0.157971  0.321231

#  plt.figure(figsize=(40,3))
#  df.plot.scatter(x='a', y='b', c='red', s=50, figsize=(40,3))
#  df.plot(kind='scatter', x='a', y='b', c='red', s=50, figsize=(40,3))

#  plt.style.use('ggplot')
#  df['a'].plot.hist(alpha=.5, bins=25, color='r')

#  plt.style.use('ggplot')
#  df[['a', 'b']].plot.box()

#  plt.style.use('ggplot')
#  df['d'].plot.kde(lw=5, ls='--')

#  plt.style.use('ggplot')
#  df[:30].plot.area(alpha=.5)

f = plt.figure()
df[0:30].plot.area(alpha=0.4,ax=f.gca())
plt.legend(loc='center left', bbox_to_anchor=(1.0, 0.5))

plt.show()