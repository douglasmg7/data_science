#!/usr/bin/env python

import numpy as np
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

df1 = pd.read_csv('df1', index_col=0)
df2 = pd.read_csv('df2',)

#  print(df1.head())
                   #  A         B         C         D
#  2000-01-01  1.339091 -0.163643 -0.646443  1.041233
#  2000-01-02 -0.774984  0.137034 -0.882716 -2.253382
#  2000-01-03 -0.921037 -0.482943 -0.417100  0.478638
#  2000-01-04 -1.738808 -0.072973  0.056517  0.015085
#  2000-01-05 -0.905980  1.778576  0.381918  0.291436


#  print(df2.head())
          #  a         b         c         d
#  0  0.039762  0.218517  0.103423  0.957904
#  1  0.937288  0.041567  0.899125  0.977680
#  2  0.780504  0.008948  0.557808  0.797510
#  3  0.672717  0.247870  0.264071  0.444358
#  4  0.053829  0.520124  0.552264  0.190008

#  df1['A'].hist(bins=30)

#  df1['A'].plot(kind='hist', bins=30)

#  df1['A'].plot.hist(bins=300)

#  df2.plot.area()

#  df2.plot.bar()
#  df2.plot.bar(stacked=True)

#  df1.plot.line(x=df1.index, y='B')   # not working

#  df1.plot.line(x=df1.index,y='B',figsize=(12,3),lw=1)     # not working

#  df1.plot.scatter(x='A', y='B')
#  df1.plot.scatter(x='A', y='B', c='C', cmap='coolwarm')    # c for color
#  df1.plot.scatter(x='A', y='B', s=df1['C']*80)    # c for color

#  df2.plot.box()

#  df = pd.DataFrame(np.random.randn(1000, 2), columns=['a', 'b'])
#  df.plot.hexbin(x='a', y='b')

#  df = pd.DataFrame(np.random.randn(1000, 2), columns=['a', 'b'])
#  df.plot.hexbin(x='a',y='b',gridsize=25,cmap='Oranges')

#  df = pd.DataFrame(np.random.randn(1000, 2), columns=['a', 'b'])
#  df.plot.hexbin(x='a',y='b',gridsize=25,cmap='coolwarm')

#  df2['a'].plot.kde()

df2.plot.kde()

plt.show()